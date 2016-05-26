# Ptyme
> The stupid terminal timer

A little baby program that just counts down.  Maybe some day it will be
daemonized and somewhat good.  That day is not today.

### Planned Features
- [ ] count down(obviously)
- [ ] keep track of multiple timers(daemon?) _(write PID to file)_
- [ ] log to file(s)
- [ ] OS agnostic pop-up window
- Timer operations
    * [ ] add
    * [ ] remove
    * [ ] list
    * [ ] edit
    * [ ] save(what?)
    * [ ] load(what?)
    * [ ] pause
    * [ ] restart
- [ ] take over world

### Example Use Case(early dev)
- `$ptyme status` : `ptyme not started`
- `$ptyme start` : `ptyme started, loaded 0 ptymer(s)`
- `$pytme status` : `pytme running, 0 ptymer(s)`
- `$ptyme list` : `no ptymers` _(could also be blank)_
- `$ptyme add 30s timeout` : `ptymer 'timeout' added for 30s`
- `$ptyme list` : `'timeout' : RUN : 29s`
- `$ptyme pause timeout` : `ptymer 'timeout' paused: 28s`
- `$ptyme add 1m` : `ptymer 'ptymer001' added for 1m`
- `$ptyme pause all` : `all ptymers paused`
- `$ptyme list timout` : `'timeout' : PAUSE : 28s`
- `$ptyme restart 001` : `ptymer 'ptymer001' restarted, 1m`
- `$ptyme play timer` : `ptymer 'timer' not found`
- `$ptyme remove all` : `all ptymers removed`
- `$ptyme stop` : `saving 0 tymer(s), stopping ptyme`
- `$ptyme status` : `ptyme not started`
