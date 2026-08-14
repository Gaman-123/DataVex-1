from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class RoleLevel(str, Enum):
    junior = "junior"
    mid    = "mid"
    senior = "senior"
    staff  = "staff"

class Track(str, Enum):
    conceptual   = "conceptual"
    lc           = "lc"
    realworld    = "realworld"
    resume_drill = "resume_drill"

class NextAction(str, Enum):
    follow_up     = "follow_up"
    stress_test   = "stress_test"
    next_question = "next_question"
    switch_track  = "switch_track"
    close         = "close"

class HireSignal(str, Enum):
    strong_yes = "strong_yes"
    yes        = "yes"
    lean_yes   = "lean_yes"
    lean_no    = "lean_no"
    no         = "no"

class CompanyRequirements(BaseModel):
    role_name:              str
    role_level:             RoleLevel
    must_have_skills:       List[dict]
    nice_to_have_skills:    List[dict] = []
    dealbreakers:           List[str]  = []
    evaluation_weights:     dict       = {"conceptual":0.35,"lc":0.25,"realworld":0.25,"resume_drill":0.15}
    min_project_proof:      int        = 1
    recency_window_months:  int        = 24
    red_flag_patterns:      List[str]  = []
    enable_lc_rounds:       bool       = True
    lc_difficulty_cap:      str        = "med_allowed"
    enable_rw_scenarios:    bool       = True
    rw_depth:               str        = "mid_level"

class ResumeAnalysis(BaseModel):
    fit_score:          float
    missing_skills:     List[str]
    unproven_claims:    List[str]
    attack_vectors:     List[dict]
    lc_topic_hints:     List[str]
    rw_scenario_seeds:  List[dict]
    dealbreaker_flags:  List[str]
    summary:            str

class EvaluatorOutput(BaseModel):
    understanding_level:      str
    content_score:            float
    next_action:              NextAction
    signals:                  dict
    requisite_skill_updated:  Optional[str] = None
    requisite_new_level:      Optional[str] = None

class VoiceOutput(BaseModel):
    confidence_level:      float
    hesitation_map:        dict
    misalignment_flag:     bool
    misalignment_type:     Optional[str] = None
    lc_narration_quality:  Optional[str] = None
    rw_polish_detected:    bool

class OrchestratorOutput(BaseModel):
    next_action:      NextAction
    next_track:       Optional[Track] = None
    next_question:    Optional[str]   = None
    hr_nudge:         str
    requisite_alert:  Optional[str]   = None