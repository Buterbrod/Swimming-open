



# This collection contains all results of a athlete or relay team of a meet
class RESULTS:
  result RESULT   # Data of one single result


# This element is used to describe one session of a meet
class SESSION:
  course e -      # With indicating a pool length per session, the global value of the meet can be overridden,
                  # e.g. if the prelim sessions are short course and the finals are long course. 
                  # See section 5.4. for acceptable values.
  date d r        # The date of the session
  daytime t -     # The daytime when the session starts.
  endtime t -     # The time when the session ended
  EVENTS o r      # The events of the session.
  FEES o          # Fees used for this session. On this level, different global fees for
                  # clubs, athletes and relays are allowed. If there are fees that have to be
                  # paid per entry, the FEE element in the EVENT objects should be used.
  JUDGES o        # The judges of the session.
  maxentriesathlete n   # The maximum number of individual entries per athlete in this session.
  maxentriesrelay n     # The maximum number of relay entries per club in this session.
  name s          # Additional name for the session e.g. "Day 1 - Prelims".
  number n r      # The number of the session. Session numbers in a meet have to be unique.
  officialmeeting t - # The daytime when the officials meeting starts.
  POOL o -        # The details about the pool, if they are different per session. Otherwise use the element in MEET.
  remarksjudge s -  # Additional remarks given by the referee.
  teamleadermeeting t -# The daytime when the team leaders meeting starts.
  timing e -      # The type of timing for a session. If missing, the global value for the meet should be used.
                  # See MEET for acceptable values.
  warmupfrom t    # The daytime when the warmup starts.
  warmupuntil t   # The daytime when the warmup ends


# Depending on the context this collection contains all sessions of a meet or all sessions for a judge, where he is planed in.
Class SESSIONS:
  SESSION o m # Data of one session

# This element contains information about a single split time. In a Lenex file, split times are always saved continuously
Class SPLIT:
  distance n r    # The distance where the split time was measured.
  swimtime st r   # The time of the result in the swim time format.
  
# This collection contains all available split times for a single result.
Class SPLITS:
  SPLIT o m       # Data of one split time.
  
# This element is used to describe one swim style
class SWIMSTYLE:
    code: str       # A code (max. 6 characters) of the swim style if the stroke is unknown.
    distance: int   # The distance for the event.
                    # For relay events it is the distance for one single athlete.
    name: str       # The full descriptive name of the swim style
                    # if the stroke is unknown (e.g. "5 x 75m Breast with one Arm only").
    relaycount: int # The number of swimmers per entry / result.
                    # Value 1 means, that it is an individual event. All other values mean, that it is a relay event.
    stroke e r      # The following values are allowed here:
                    # * APNEA: for apnea (fin swimming).
                    # * BACK: for backstroke.
                    # * BIFINS: for bi-fins (fin swimming).
                    # * BREAST: for breaststroke.
                    # * FLY: for fly or butterfly.
                    # * FREE: for freestyle.
                    # * IMMERSION: for immersion (fin swimming).
                    # * IMRELAY: for relays where each athletes swims all strokes like in an individual medley event.
                    # * MEDLEY: for individual and relay medley. The order of stroke is
                    #   according to FINA rules: Fly, back, breast, free for individual
                    #   events. Back, breast, fly, free for relay events.
                    # * SURFACE: for surface (fin swimming).
                    # * UNKNOWN: for all special events. In this case, the name attribute
                    #   of the event is mandatory.
    swimstyleidL: int    # The id attribute is important for SWIMSTYLE objects, where the stroke
                    # attribute is "UNKNOWN". In this case, the id should be a unique value
                    # to help to identify the swim style.
    technique: e    # The technique of the style. If this attribute is missing or empty, it
                    # means normal swimming. All other values are mainly used for
    technical events in meets for kids. The following values are allowed:
* DIVE: for swimming under water.
* GLIDE: for gliding only.
* KICK: for kick only (Swimming with legs, no arms used).
* PULL: for pull only (Swimming with arms, no legs used).
* START: for start only.
* TURN: for turn only.
