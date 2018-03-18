# VARIABLES
#   tries: The maximum number of attempts of accessing url
#   delay: The delay in amount of seconds after the first failed attempt
# backoff: Multiplier for exponential growth used for the calculation of delay for subsequent failed attempts. If backoff is 2, 2nd failed attempt delay is 2*delay, 3rd failed attempt delay is 2*2*delay, 4th failed attempt delay is 2*2*2*delay, and so on.
config = {
  "tries": 7,
  "delay": 60,
"backoff": 2
}
