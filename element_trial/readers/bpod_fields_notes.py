'''Temporary file for keeping track of bpod structures

The RAW prefix in bpod structures seems to always have data elsewhere
	Raw is where it is initially stored, and then ported elsewhere during export

Inconsistent across examples:
	BalbC top level: LeftValveTime, RightValveTime, LeftAmount, RightAmount,changebridge, bridgepos, subject, delays
	1119a top level: Notes, MarkerCodes

Custom is determined by user:
	1119a Custom: contrastLevels, dbSplTrialType3, dbSplTrialType6,startSessionDatetime, startSessionTimeStamp,TQ03_Dual2AFC_Jun18_2021_Session1.mat, BlockNumber,BlockTrial, ChoiceLeft, ChoiceCorrect, Feedback, FeedbackTimeFixBroke, EarlyWithdrawal, FixDur, MT, CatchTrial, OdorFracA,OdorID, OdorPair, ST, ResolutionTime, Rewarded,RewardMagnitude, number_trials, LaserTrial,LaserTrialTrainStart, AuditoryTrial, ClickTask,OlfactometerStartup, PsychtoolboxStartup, AuditoryOmega,LeftClickRate, RightClickRate, LeftClickTrain,RightClickTrain, LeftRewarded, DV, Rig, Subject,PulsePalParamStimulus, PulsePalParamFeedback, StimDelay,FeedbackDelay, MinSampleAud,
	TP24 Custom: BlockNumber, BlockTrial, ChoiceLeft, ChoiceCorrect, Feedback,FeedbackTime, FixBroke, EarlyWithdrawal, FixDur, MT,CatchTrial, OdorFracA, OdorID, OdorPair, ST, Rewarded,RewardMagnitude, number_trials, LaserTrial, LaserTrialTrainStart,AuditoryTrial, ClickTask, OlfactometerStartup,PsychtoolboxStartup, AuditoryOmega, LeftClickRate,RightClickRate, LeftClickTrain, RightClickTrain, LeftRewarded,DV, Rig, Subject, PulsePalParamStimulus, PulsePalParamFeedback,StimDelay, FeedbackDelay, MinSampleAud

Settings is inconsistently used:
	BalcC: Nothing
	TQ03 : same as TrialSettings

TrialSettings is also file-specific:
	BalbC TrialSettings: Subject, RewardAmount, RewardDelay, ChangeOver, block, depleft, depright, MaxTrials, randomDelay, Lange, Bridge, Drugs
	1119A TrialSettings: MaxTrialNum, StartPhaseLength, TrialType1, TrialType2,TrialType3, TrialType4, TrialType5, TrialType6, TrialType7, RewardAmount, ContrastLevelMin, ContrastLevelMax, UseBonsai, UsePulsePal, PulsePalComPort, PulsePalParameterFile, UseOptoGeneticPulseLength, NumberOfPulses, PulseFrequency,Bpod_BNC_Ch_Opto, PulsePal_Trig_Ch_Opto, PulsePal_Out_Ch_Opto, Opto_Stim_In_TrialType2, Opto_Stim_In_TrialType3, Opto_Stim_In_TrialType5, Opto_Stim_In_TrialType6, UseSoundStimulation, dB_SPL_min, dB_SPL_max, dB_SPL_step, Photometry, DbleFibers, Isobestic405, RedChannel,PhotometryVersion, Modulation, NidaqDuration, NidaqSamplingRate, DecimateFactor, LED1_Name, LED1_Amp, LED1_Freq, LED2_Name, LED2_Amp, LED2_Freq, LED1b_Name, LED1b_Amp, LED1b_Freq
	TQ03_ TrialSettings: Aud_Levels, Aud_NoEvidence, Aud_Ramp, Aud_SamplingRate, Aud_ToneDuration, Aud_ToneOverlap, Aud_UseMiddleOctave, Aud_Volume, Aud_maxFreq, Aud_minFreq, Aud_nFreq, AuditoryAlpha, AuditoryStimulusTime, AuditoryStimulusType, BaselineBegin, BaselineEnd, BlockTable, CatchError, CenterWaitMax, ChoiceDeadLine, DbleFibers, DecimateFactor, DrinkingGrace, DrinkingTime, FeedbackDelay, FeedbackDelayDecr, FeedbackDelayGrace, FeedbackDelayIncr, FeedbackDelayMax, FeedbackDelayMin, FeedbackDelaySelection, FeedbackDelayTau, ITI, IncorrectChoiceFeedbackType, Isobestic405, LED1_Amp, LED1_Freq, LED1_Name, LED1b_Amp, LED1b_Freq, LED1b_Name, LED2_Amp, LED2_Freq, LED2_Name, LaserAmp, LaserFeedback, LaserITI, LaserMov, LaserPreStim, LaserPulseDuration_ms, LaserRampDuration_ms, LaserRew, LaserSoftCode, LaserStim, LaserStimFreq, LaserTimeInvestment, LaserTrainDuration_ms, LaserTrainRandStart, LaserTrainStartMax_s, LaserTrainStartMin_s, LaserTrials, LeftBiasAud, MaxSessionTime, MinSampleAud, MinSampleAudAutoincrement, MinSampleAudDecr, MinSampleAudIncr, MinSampleAudMax, MinSampleAudMin, Modulation, NidaqDuration, NidaqMax, NidaqMin, NidaqSamplingRate, OdorA_bank, OdorB_bank, OdorStimulusTimeMin, OdorTable, Percent50Fifty, PercentAuditory, PercentCatch, PhotoPlotReward, PhotoPlotSidePokeIn, PhotoPlotSidePokeLeave, Photometry, PhotometryVersion, PortLEDs, Ports_LMR, PreITI, RedChannel, RewardAmount, ShowFeedback, ShowFix, ShowPsycAud, ShowPsycOlf, ShowST, ShowTrialRate, ShowVevaiometric, SkippedFeedbackFeedbackType, StartEasyTrials, StimDelay, StimDelayAutoincrement, StimDelayDecr, StimDelayIncr, StimDelayMax, StimDelayMin, SumRates, TimeMax, TimeMin, TimeOutBrokeFixation, TimeOutEarlyWithdrawal, TimeOutIncorrectChoice, TimeOutSkippedFeedback, TrialSelection, VevaiometricMinWT, VevaiometricNBin, VevaiometricShowPoints, VideoTrials, Wire1VideoTrigger, nidaqDev
	TP24_ TrialSettings: Aud_Levels, Aud_NoEvidence, Aud_Ramp, Aud_SamplingRate, Aud_ToneDuration, Aud_ToneOverlap, Aud_UseMiddleOctave, Aud_Volume, Aud_maxFreq, Aud_minFreq, Aud_nFreq, AuditoryAlpha, AuditoryStimulusTime, AuditoryStimulusType, BlockTable, CatchError, ChoiceDeadLine, FeedbackDelay, FeedbackDelayDecr, FeedbackDelayGrace, FeedbackDelayIncr, FeedbackDelayMax, FeedbackDelayMin, FeedbackDelaySelection, FeedbackDelayTau, ITI, IncorrectChoiceFeedbackType, LaserFeedback, LaserITI, LaserMov, LaserPreStim, LaserPulseDuration_ms, LaserRew, LaserStim, LaserStimFreq, LaserTimeInvestment, LaserTrainDuration_ms, LaserTrainRandStart, LaserTrainStartMax_s, LaserTrainStartMin_s, LaserTrials, LeftBiasAud, MaxSessionTime, MinSampleAud, MinSampleAudAutoincrement, MinSampleAudDecr, MinSampleAudIncr, MinSampleAudMax, MinSampleAudMin, OdorA_bank, OdorB_bank, OdorStimulusTimeMin, OdorTable, Percent50Fifty, PercentAuditory, PercentCatch, PortLEDs, Ports_LMR, RewardAmount, ShowFeedback, ShowFix, ShowPsycAud, ShowPsycOlf, ShowST, ShowTrialRate, ShowVevaiometric, SkippedFeedbackFeedbackType, StartEasyTrials, StimDelay, StimDelayAutoincrement, StimDelayDecr, StimDelayIncr, StimDelayMax, StimDelayMin, SumRates, TimeOutBrokeFixation, TimeOutEarlyWithdrawal, TimeOutIncorrectChoice, TimeOutSkippedFeedback, TrialSelection, VevaiometricMinWT, VevaiometricNBin, VevaiometricShowPoints, Wire1VideoTrigger

TrialTypes: array of condition? Not consistent across all trials

['SessionData'].RawEvents.Trial[0].States
BalbC_Ph_W1_LH_Randdelay_changeover_Aug08_2021_Session1.mat
RawEvents
RawData

Bonn bpod SessionData structure
	TrialTypes - 1,2,3,1,2,3
	TrialTypeNames - Visibile,Visible,Fading
	Info
		StateMachineVersion
		SessionDate
		SessionStartTime_UTC
		SessionStartTime_MATLAB
	nTrials (# trials in session, here 54)
	RawEvents (timestamps for each trial's state transitions/recorded events)
		Trial{1,n}.States #Which of these are important?
			WaitForPosTriggerSoftCode
			CueDelay
			WaitForResponse
			Port2RewardDelay
			Port2Reward
			CloseValves
			Drinking
			Port1RewardDelay
			Port3RewardDelay
			Port4RewardDelay
			Port5RewardDelay
			Port6RewardDelay
			Port7RewardDelay
			Port8RewardDelay
			Port1Reward
			Port3Reward
			Port4Reward
			Port5Reward
			Port6Reward
			Port7Reward
			Port8Reward
			Punish
			Punishexit
			EarlyWithdrawal
		Trial{1,n}.Events
			Port4In
			Port4Out
			SoftCode10
			Tup
			Port2In
			Port2Out
	RawData (copy of raw data from state machine)
	TrialStartTimestamp (time when trial started on Bpod's clock)
		Note: Timestamps in RawEvents are relative to each trial's start
	TrialEndTimestamp
	SettingsFile (the settings file you selected in the launch manager)
	Notes
	MarkerCodes
	CurrentSubjectName
	TrialSettings
		GUI
		GUIMeta
		GUIPanels
		polling
		debug
		debugvis
		Data
		arm_number
		arm_baited_orig
		arm_baited
		SF
		rotation
		position
		StimAlpha
	StimPos
		TriggerLocPix
		TriggerLocOptitrackHitbox
		TriggerLocOptitrackCenter
		TriggerLocOptitrackCircleHitRadius
		tform
'''
'''
