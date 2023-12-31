level_maps = [[
'                              ',
'                              ',
'XX    XXX        XX        XXX',
'                              ',
'   P                           ',
'XXXXXXXXX   XXXXXXXXXXXX  XXXXXX',
'XXXXXXXX   XXXXXXXXXXXX  XXXXXX',
'XXXXXXXXX   XXXXXXXXXXXXX  XXXXX',
'XXXXXXXXX   XXXXXXXXXXXXX  XXXXXX',
'XXXXXXXXX   XXXXXXXXXXXXX  XXXXX'],
[
'                              ',
'                              ',
'XX    XXX        XX        XXX',
'                              ',
'      P                        ',
'  XXXXXXX   XXXXX  XXXXX  XXXXXX',
'  XXXXXXX   XXXXX  XXXXX  XXXXXX',
'  XXXXXXX   XXXXX  XXXXXX  XXXXX',
'  XXXXXXX   XXXXX  XXXXXX  XXXXXX',
'  XXXXXXX   XXXXX  XXXXXX  XXXXX'],
[
'                              ',
'                              ',
'XX    XXX        XX        XXX',
'                              ',
'             P                 ',
'  XXXXXXX   XXX XXXXXXXX  XXXXXX',
'  XXXXXXX   XXX XXXXXXXX  XXXXXX',
'  XXXXXXX   XXX XXXXXXXXX  XXXXX',
'  XXXXXXX   XXX XXXXXXXXX  XXXXXX',
'  XXXXXXX   XXX XXXXXXXXX  XXXXX'],
[
'                              ',
'                              ',
'XX    XXX        XX        XXX',
'                              ',
'   P           XX                ',
'  XX XXXX   XXXXX    XXX  XXXXXX',
'  XX XXXX   XXXXX    XXXX  XXXXXX',
'  XX XXXX   XXXXXX  XXXXXXX  XXXXX',
'  XX XXXX   XXXXXX     XXXXX  XXXXXX',
'  XX XXXX   XXXXXXX   XXXX  XXXXX'],
[
'                              ',
'                              ',
'XX    XXX        XX        XXX',
'                              ',
'    P                           ',
'  XXXXX XX   XX  XX   XX  XX        XXXX',
'  XXXXX XX   XX  XX      XXX        XX  XXXXXX',
'  XXXXX XX   XX   XXXX      XXX     X  XXXXX',
'  XXXXX XX   XX   XX     XXXXX      X  XXXXXX',
'  XXXXX XX   XX   XXXXXXXX  XXX     X'],
[
'                              ',
'                              ',
'XX    XX        XX        XXX',
'            XX                  ',
'      P                        ',
'  XXXXXXX   XXXX   XX  XX        XXXX',
'  XXXXXXX   XXXXX      XXX        XX  XXXXXX',
'  XXXXXXX   XXXXXXX      XXX     X  XXXXX',
'  XXXXXXX   XXXXXXX     XXXXX      X  XXXXXX',
'  XXXXXXX   XXXXXXXXXXXXX  XXX     X'],
[
'                              ',
'                              ',
'XX    XXX        XX        XXX',
'                              ',
'      P                        ',
'  XXXXXXX   XX     X X   XX  XX        XXXX',
'  XXXXXXX   XX    XXX      XXX        XX  XXXXXX',
'  XXXXXXX   XXX    XXXX      XXX     X  XXXXX',
'  XXXXXXX   XXX    XXXX     XXXXX      X  XXXXXX',
'  XXXXXXX   XXXX     XXXXXXXXX  XXX     X']]
#design level makeup
#Different levels, that will be infinetely looping as character runs through
tile_size = 50

max_level_width = 720
screen_width = 1200
screen_height = len(level_maps[0]) * tile_size

#this is how the level resets, it chooses a random map to set our play to, once player reaches the max level width it resets  
#one of our unique aspects that is different to the inspiration video
