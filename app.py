from flask import Flask, session, redirect, url_for, request
from flask import render_template
from markupsafe import escape
from dragonballweb import scenes
import random

app = Flask(__name__)

@app.route('/')
def index():
    # this is used to 'setup' the session with starting values
    session['scene_name'] = scenes.START
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    scene_name = session.get('scene_name')
    print('in game function')
    print(f'scene name is {scene_name}')

    if request.method == 'GET':
        print('request method GET')
        if scene_name:
            print('if scene name was true')
            scene = scenes.load_scene(scene_name)
            return render_template('show_scene.html', scene=scene)
        else:
            # why is this here? do you need it?'
            return render_template('you_died.html')
    else:
        print('request method POST')
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

@app.route('/chartreuse', methods=["GET", "POST"])
def color_check():
    current_scene = session.get('scene_name')
    print(f'current scene is {current_scene}')

    char_col = request.args.get('char_col')

    # checks for a color argument
    # if present, passes that to the description
    if char_col:
        print(f'got char_col of {char_col}')
        scenes.green = char_col
        print(f'green is now {scenes.green}')
    # if not present, pulls the random color from the program
    else:
        char_col = scenes.green
        print(f'no color given, loaded {scenes.green}')
        print(f'also set char_col to {char_col}')

    # if we made it to green, loads the version with choices
    if 'green' not in char_col:
        scene = scenes.load_scene('chartreuse')
    else:
        print('in else block')
        scene = scenes.load_scene('chartreuse_green')
        session['scene_name'] = 'round1'
        scene_name = session.get('scene_name')
        action = request.form.get('action')
        print(f'session object is {session}')

        if scene_name and action:
            scene = scenes.load_scene(scene_name)
            print(f'loading scene {scene_name}')
            next_scene = scene.choose('*')
            print(f'next scene is {next_scene}')

            if not next_scene:
                print('landed if not')
                session['scene_name'] = scenes.name_scene(scene)
            else:
                print('landed else')
                session['scene_name'] = scenes.name_scene(next_scene)
                return redirect(url_for('game'))

    return render_template('chartreuse.html', scene=scene, char_col=char_col)

# change this if you put it on the internet
app.secret_key = 'blahblahblahblahblah'

if __name__ == '__main__':
    app.run(debug=True)
