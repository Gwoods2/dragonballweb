from flask import Flask, session, redirect, url_for, request
from flask import render_template
from markupsafe import escape
from dragonballweb import scenes

app = Flask(__name__)

@app.route('/')
def index():
    # this is used to 'setup' the session with starting values
    session['scene_name'] = scenes.START
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    scene_name = session.get('scene_name')

    if request.method == 'GET':
        if scene_name:
            scene = scenes.load_scene(scene_name)
            return render_template('show_scene.html', scene=scene)
        else:
            # why is this here? do you need it?'
            return render_template('you_died.html')
    else:
        raw_action = request.form.get('action')
        syn_action = scenes.thesaurus(raw_action)

        if scene_name and syn_action:
            scene = scenes.load_scene(scene_name)
            next_scene = scene.choose(syn_action)

            if not next_scene:
                session['scene_name'] = scenes.name_scene(scene)
            else:
                session['scene_name'] = scenes.name_scene(next_scene)

        return redirect(url_for('game'))
    
@app.route("/next", methods=["GET"])
def next_scene():
  current_scene = session.get('scene_name')

  scene = scenes.load_scene(current_scene)
  next_scene = scene.choose('next')

  if not next_scene:
    session['scene_name'] = scenes.name_scene(scene)
  else:
    session['scene_name'] = scenes.name_scene(next_scene)

  return redirect(url_for('game'))

@app.route("/back", methods=["GET"])
def back_scene():
  current_scene = session.get('scene_name')

  scene = scenes.load_scene(current_scene)
  next_scene = scene.choose('back')

  if not next_scene:
    session['scene_name'] = scenes.name_scene(scene)
  else:
    session['scene_name'] = scenes.name_scene(next_scene)

  return redirect(url_for('game')) 

# change this if you put it on the internet
app.secret_key = 'blahblahblahblahblah'

if __name__ == '__main__':
    app.run(debug=True)
