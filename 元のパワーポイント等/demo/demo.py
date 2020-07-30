#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on 7月 29, 2020, at 11:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'demo'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\asako\\OneDrive\\デスクトップ\\demo\\demo.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial_cross"
trial_crossClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
o1 = visual.ImageStim(
    win=win,
    name='o1', 
    image='o1.PNG', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
o2 = visual.ImageStim(
    win=win,
    name='o2', 
    image='o2.PNG', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
o3 = visual.ImageStim(
    win=win,
    name='o3', 
    image='o3.PNG', mask=None,
    ori=0, pos=(0.25,0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "trial_chosen"
trial_chosenClock = core.Clock()
Left_2 = visual.Rect(
    win=win, name='Left_2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(-0.25, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Mid_2 = visual.Rect(
    win=win, name='Mid_2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Right_2 = visual.Rect(
    win=win, name='Right_2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0.25, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
o1_2 = visual.ImageStim(
    win=win,
    name='o1_2', 
    image='o1.PNG', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
o2_2 = visual.ImageStim(
    win=win,
    name='o2_2', 
    image='o2.PNG', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
o3_2 = visual.ImageStim(
    win=win,
    name='o3_2', 
    image='o3.PNG', mask=None,
    ori=0, pos=(0.25, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
gray1 = visual.ImageStim(
    win=win,
    name='gray1', 
    image='gray.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=0.8,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
gray2 = visual.ImageStim(
    win=win,
    name='gray2', 
    image='gray.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=0.8,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_cross"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    trial_crossComponents = [text]
    for thisComponent in trial_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_crossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_cross"-------
    for thisComponent in trial_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    trialComponents = [mouse, o1, o2, o3]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # *o1* updates
        if o1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o1.frameNStart = frameN  # exact frame index
            o1.tStart = t  # local t and not account for scr refresh
            o1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o1, 'tStartRefresh')  # time at next scr refresh
            o1.setAutoDraw(True)
        
        # *o2* updates
        if o2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o2.frameNStart = frameN  # exact frame index
            o2.tStart = t  # local t and not account for scr refresh
            o2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o2, 'tStartRefresh')  # time at next scr refresh
            o2.setAutoDraw(True)
        
        # *o3* updates
        if o3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o3.frameNStart = frameN  # exact frame index
            o3.tStart = t  # local t and not account for scr refresh
            o3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o3, 'tStartRefresh')  # time at next scr refresh
            o3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    trials.addData('mouse.leftButton', buttons[0])
    trials.addData('mouse.midButton', buttons[1])
    trials.addData('mouse.rightButton', buttons[2])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    if mouse.isPressedIn(o1):
        gray1_posi = (0,0)
        gray2_posi = (0.25,0)
    if mouse.isPressedIn(o2):
        gray1_posi = (-0.25,0)
        gray2_posi = (0.25,0)
    if mouse.isPressedIn(o3):
        gray1_posi = (-0.25,0)
        gray2_posi = (0,0)
    trials.addData('o1.started', o1.tStartRefresh)
    trials.addData('o1.stopped', o1.tStopRefresh)
    trials.addData('o2.started', o2.tStartRefresh)
    trials.addData('o2.stopped', o2.tStopRefresh)
    trials.addData('o3.started', o3.tStartRefresh)
    trials.addData('o3.stopped', o3.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_chosen"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    gray1.setPos(gray1_posi)
    gray2.setPos(gray2_posi)
    # keep track of which components have finished
    trial_chosenComponents = [Left_2, Mid_2, Right_2, o1_2, o2_2, o3_2, gray1, gray2]
    for thisComponent in trial_chosenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_chosenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_chosen"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_chosenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_chosenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Left_2* updates
        if Left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Left_2.frameNStart = frameN  # exact frame index
            Left_2.tStart = t  # local t and not account for scr refresh
            Left_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Left_2, 'tStartRefresh')  # time at next scr refresh
            Left_2.setAutoDraw(True)
        if Left_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Left_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Left_2.tStop = t  # not accounting for scr refresh
                Left_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Left_2, 'tStopRefresh')  # time at next scr refresh
                Left_2.setAutoDraw(False)
        
        # *Mid_2* updates
        if Mid_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Mid_2.frameNStart = frameN  # exact frame index
            Mid_2.tStart = t  # local t and not account for scr refresh
            Mid_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Mid_2, 'tStartRefresh')  # time at next scr refresh
            Mid_2.setAutoDraw(True)
        if Mid_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Mid_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Mid_2.tStop = t  # not accounting for scr refresh
                Mid_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Mid_2, 'tStopRefresh')  # time at next scr refresh
                Mid_2.setAutoDraw(False)
        
        # *Right_2* updates
        if Right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Right_2.frameNStart = frameN  # exact frame index
            Right_2.tStart = t  # local t and not account for scr refresh
            Right_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Right_2, 'tStartRefresh')  # time at next scr refresh
            Right_2.setAutoDraw(True)
        if Right_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Right_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Right_2.tStop = t  # not accounting for scr refresh
                Right_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Right_2, 'tStopRefresh')  # time at next scr refresh
                Right_2.setAutoDraw(False)
        
        # *o1_2* updates
        if o1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o1_2.frameNStart = frameN  # exact frame index
            o1_2.tStart = t  # local t and not account for scr refresh
            o1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o1_2, 'tStartRefresh')  # time at next scr refresh
            o1_2.setAutoDraw(True)
        if o1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > o1_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                o1_2.tStop = t  # not accounting for scr refresh
                o1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(o1_2, 'tStopRefresh')  # time at next scr refresh
                o1_2.setAutoDraw(False)
        
        # *o2_2* updates
        if o2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o2_2.frameNStart = frameN  # exact frame index
            o2_2.tStart = t  # local t and not account for scr refresh
            o2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o2_2, 'tStartRefresh')  # time at next scr refresh
            o2_2.setAutoDraw(True)
        if o2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > o2_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                o2_2.tStop = t  # not accounting for scr refresh
                o2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(o2_2, 'tStopRefresh')  # time at next scr refresh
                o2_2.setAutoDraw(False)
        
        # *o3_2* updates
        if o3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o3_2.frameNStart = frameN  # exact frame index
            o3_2.tStart = t  # local t and not account for scr refresh
            o3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o3_2, 'tStartRefresh')  # time at next scr refresh
            o3_2.setAutoDraw(True)
        if o3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > o3_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                o3_2.tStop = t  # not accounting for scr refresh
                o3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(o3_2, 'tStopRefresh')  # time at next scr refresh
                o3_2.setAutoDraw(False)
        
        # *gray1* updates
        if gray1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gray1.frameNStart = frameN  # exact frame index
            gray1.tStart = t  # local t and not account for scr refresh
            gray1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gray1, 'tStartRefresh')  # time at next scr refresh
            gray1.setAutoDraw(True)
        if gray1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gray1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                gray1.tStop = t  # not accounting for scr refresh
                gray1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gray1, 'tStopRefresh')  # time at next scr refresh
                gray1.setAutoDraw(False)
        
        # *gray2* updates
        if gray2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gray2.frameNStart = frameN  # exact frame index
            gray2.tStart = t  # local t and not account for scr refresh
            gray2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gray2, 'tStartRefresh')  # time at next scr refresh
            gray2.setAutoDraw(True)
        if gray2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > gray2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                gray2.tStop = t  # not accounting for scr refresh
                gray2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(gray2, 'tStopRefresh')  # time at next scr refresh
                gray2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_chosenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_chosen"-------
    for thisComponent in trial_chosenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Left_2.started', Left_2.tStartRefresh)
    trials.addData('Left_2.stopped', Left_2.tStopRefresh)
    trials.addData('Mid_2.started', Mid_2.tStartRefresh)
    trials.addData('Mid_2.stopped', Mid_2.tStopRefresh)
    trials.addData('Right_2.started', Right_2.tStartRefresh)
    trials.addData('Right_2.stopped', Right_2.tStopRefresh)
    trials.addData('o1_2.started', o1_2.tStartRefresh)
    trials.addData('o1_2.stopped', o1_2.tStopRefresh)
    trials.addData('o2_2.started', o2_2.tStartRefresh)
    trials.addData('o2_2.stopped', o2_2.tStopRefresh)
    trials.addData('o3_2.started', o3_2.tStartRefresh)
    trials.addData('o3_2.stopped', o3_2.tStopRefresh)
    trials.addData('gray1.started', gray1.tStartRefresh)
    trials.addData('gray1.stopped', gray1.tStopRefresh)
    trials.addData('gray2.started', gray2.tStartRefresh)
    trials.addData('gray2.stopped', gray2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
