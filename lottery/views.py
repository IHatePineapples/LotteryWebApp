# IMPORTS
import logging
import copy

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from app import db
from models import Draw, User

# CONFIG
lottery_blueprint = Blueprint('lottery', __name__, template_folder='templates')


# VIEWS
# view lottery page
@lottery_blueprint.route('/lottery')
@login_required
def lottery():
    return render_template('lottery.html')


@lottery_blueprint.route('/add_draw', methods=['POST'])
@login_required
def add_draw():
    submitted_draw = ''
    for i in range(6):
        submitted_draw += request.form.get('no' + str(i + 1)) + ' '
    submitted_draw.strip()

    # create a new draw with the form data.
    new_draw = Draw(user_id=current_user.id, draw=submitted_draw, win=False, round=0, draw_key=current_user.draw_key)

    # add the new draw to the database
    db.session.add(new_draw)
    db.session.commit()

    # re-render lottery.page
    flash('Draw %s submitted.' % submitted_draw)
    return lottery()


# view all draws that have not been played
@lottery_blueprint.route('/view_draws', methods=['POST'])
@login_required
def view_draws():
    # get all draws that have not been played [played=0]
    playable_draws = Draw.query.filter_by(played=False, user_id=current_user.id).all()

    # creates a list of copied draws objects which are independent of database.
    # playable_draws_copies = list(map(lambda x: copy.deepcopy(x), playable_draws))
    # This is better
    playable_draws_copies = copy.deepcopy(playable_draws)
    decrypted_playable_draws = []

    for d in playable_draws_copies:
        d.view_draw(current_user.draw_key)
        decrypted_playable_draws.append(d)

    # if playable draws exist
    if len(playable_draws) != 0:
        # re-render lottery page with playable draws
        return render_template('lottery.html', playable_draws=decrypted_playable_draws)
    else:
        flash('No playable draws.')
        return lottery()


# view lottery results
@lottery_blueprint.route('/check_draws', methods=['POST'])
@login_required
def check_draws():
    # get played draws
    played_draws = Draw.query.filter_by(played=True, user_id=current_user.id).all()
    played_draws_copies = copy.deepcopy(played_draws)
    decrypted_played_draws = []
    for d in played_draws_copies:
        d.view_draw(current_user.draw_key)
        decrypted_played_draws.append(d)

    # if played draws exist
    if len(played_draws) != 0:
        return render_template('lottery.html', results=decrypted_played_draws, played=True)

    # if no played draws exist [all draw entries have been played therefore wait for next lottery round]
    else:
        flash("Next round of lottery yet to play. Check you have playable draws.")
        return lottery()


# delete all played draws
@lottery_blueprint.route('/play_again', methods=['POST'])
@login_required
def play_again():
    delete_played = Draw.__table__.delete().filter_by(user_id=current_user.id).where(Draw.played)
    db.session.execute(delete_played)
    db.session.commit()

    flash("All played draws deleted.")
    return lottery()
