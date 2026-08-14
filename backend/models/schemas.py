from pydantic import BaseModel
from typing import Optional, List

class CompanyCreate(BaseModel):
    name:     str
    industry: Optional[str] = None

class RequirementsCreate(BaseModel):
    company_id:             str
    role_name:              str
    role_level:             str        = "mid"
    must_have_skills:       List[dict] = []
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
    lc_weight:              float      = 0.25
    rw_weight:              float      = 0.25

class CandidateCreate(BaseModel):
    company_id:      str
    full_name:       str
    email:           Optional[str] = None
    college:         Optional[str] = None
    resume_raw_text: str

class SessionCreate(BaseModel):
    candidate_id:    str
    company_id:      str
    hr_user_id:      str
    requirements_id: str

class AnswerSubmit(BaseModel):
    session_id:         str
    round_number:       int
    track:              str
    question_id:        str
    question_text:      str
    question_metadata:  dict
    answer_transcript:  str
    answer_code:        Optional[str] = None
    audio_features:     dict          = {}
    requisite_skill:    Optional[str] = None

class HROverride(BaseModel):
    session_id:        str
    override_question: str
    override_track:    Optional[str] = None