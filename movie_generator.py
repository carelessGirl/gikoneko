#!/usr/bin/env python
# -*- coding=utf-8 -*-
#Using GPL v2
## author : happybeetle
"""
Usage:
Just A Template
"""
import numpy as np

frames = [r'''
boy meets girl...

      /:""|       .@@@@@,
     |:`66|_      @@@@@@@@,
     C`    _)     aa`@@@@@@
      \ ._|      (_   ?@@@@
       ) /        =' @@@@"
      /`\\         \(```
     || |Y|       //`\
     || |.|      / | ||
     || |.|      \ | ||
     || |.|       \| ||
     :| |=:        |_|\
     ||_|,|        |_| \
     \)))||        (((  |
      |  ||        |____|
      |  ||        |____|
      >  ))         | ||
      | ||          | ||
      | ||          | ||
      |_||__        /~))
      (____))      /_/YY
''',
r'''
and fall in love...

       /:""|  .@@@@@,
(\/)  |:`66|_ @@@@@@@@,
 \/   C`    _)aa`@@@@@@
       \ ._| (_   ?@@@@
        ) /   =' @@@@"
       /`\\    \(```
      || |Y|  //`\
      || |.| / | || (\/)
      || |.| \ | ||  \/
      || |.|  \| ||
      :| |=:   |_|\
      ||_|,|   |_| \
      \)))||   (((  |
 (\/)  |  ||   |____|
  \/   |  ||   |____|
       >  ))    | ||
       | ||     | ||
       | ||     | ||
       |_||__   /~))
       (____)) /_/YY
''',
r'''
tie the knot...

       /:""|  .****,
(\/)  |:`66|_ @@@@@\ `,
 \/   C`    _)aa`@@@\  \
       \ ._| (_   ?@@|  \
        )_/   =' @@@@|   |
       /`\8\   \(```/    |
      || |8|  /^^\ |     /
      || |8| /\::/||    |
      || |8| \ | |||    \
      || |~|  \| |||     \
      :| |=:   |:|\\.:.:.::.
      ||_|,|   |:| \ ':':':`
      \)))||   (((  |
       | :||   |    | (\/)
       | :||   |    |  \/
       ) :||   |    \
       | :||   |     `\
       | :||   |:.:.   `~-._
       |_:||_   /~))\       `~~-._
       (_,__)) /_/YY `':':':':':':`
''',
r'''
boy and girl are soon to become parents...boy goes off to work...

      /:""|       .@@@@@,
     |:`66|_      @@@@@@@@,
     C`    _)     aa`@@@@@@
      \ ._|      (_   ?@@@@
       ) /        =' @@@@"
      /`\\         \(```
     || |Y|       //`\
     || |#|      / | ||
     || |#|      \ | ||
     || |#|      / | ||
     :| |=:     /  |_|\
     ||_|,|    |   |_| \
     \)))||     \  (((  |
  |~~~`-`~~~|    `\     |
  |         |      |____|
  |_________|       | ||
  |_________|       | ||
      | ||          | ||
      |_||__        /~))
      (____))      /_/YY
''',
r"""boy and girl and baby make three ...and another on the way...

      /:""|       .@@@@@,
     |:`66|_      @@@@@@@@,
     C     _)     aa`@@@@@@
      \ ._|      (_   ?@@@@
       ) /        =' @@@@"
      /`\\         \(```
     || |Y|       //`\        ."~~~~~".
     || |#|      / | ||       | (>o<) |
     || |#|      \ | ||       | /a a\ |  A
     || |#|      / | ||      _|_\ O /_|_|~|
     :| |=:     /  | |\     8)___`"`___(|_|
     ||_|,|    |   |_| \     |~~~~~~~~~|
     \)))||    |   (((  |    \_________/
  |~~~`-`~~~|  `~\~~~~~~|     |/ /_\ \|
  |         |     `\   /      ()/___\()
  |_________|       ( ||      ||~~~~~||
  |_________|       | ||      ||     ||
      | ||          | ||      ||     ||
      |_||__      __|_||      ||_____||
      (____))    (:;:;))      ||-----||
""",
r'''
boy and girl and their 2.4 children...

      /:""|       .@@@@@,
     |: 66|_      @@@@@@@@,
     C     _)     aa`@@@@@@
      \ ._|      (_   ?@@@@
       ) /        =' @@@@"
      /`\\         \(```
     || |Y|       //`\        ."~~~~~".
     || |#|      / | ||       |  .:.  |
     || |#|      \ | ||    A  | /6 6\ |
     || |#|      / | ||   |~|_|_\ e /_|_     .@@@@,
     :| |=:     /  | |\   |_|)___`"`___(8    aa`@@@,
     ||_|,|    |   |_| \     |~~~~~~~~~|     =  `@@@
     \)))||    |   (((  |    \_________/       )_/`@'
  |~~~`-`~~~|  `~\~~~~~~|     |/ /_\ \|       / || @
  |         |     `\   /      ()/___\()       | || @
  |_________|       ( ||      ||~~~~~||       /~|| "`
  |_________|       | ||      ||     ||      /__W_\
      | ||          | ||      ||     ||        |||
      |_||__      __|_||      ||_____||       _|||
      (____))    (:;:;))      ||-----||      (___))
''',
r'''
boy and girl and their growing family...

      /:`"|       .@@@@@,
     |: 66|_      @@@@@@@@,
     C     _)     aa`@@@@@@
      \ ._|      (_   ?@@@@
       ) /        =' @@@@"
      /`\\         \(```                       @@@@@,
     || |Y|       //`\        ."~~~~~".       aa`@@@@,
     || |#|      / | ||       |  .@.  |      (_   ?@@@
     || |#\      \ | ||       | /e e\ |  A     =  @@@@
     || | #|     | | ||   0 0_|_\ - /_|_|~|     )_@@@"   |"":\
     :| |==:     | | |\   ("))___`"`___(|_|    /. |@@    66 `:|
     ||_|,/      | |_| \ `( )|~~~~~~~~~|      ((| |     (_   /
     \)))||      | (((  | '^'\_________/       || |       -_(
  |~~~`-`~~~|    \~~~~~~|     |/ /_\ \|        ||_|       / ||
  |         |     \    /      ()/___\()        | W)       | ||
  |_________|     ((  |       ||~~~~~||        || |       |_||
  |_________|     ||  |       ||     ||        || |       | W|
      | ||        ||  |       ||     ||        || |       || |
      |_||__      ||__|       ||_____||       _||_|      _||_|
      (____))   ((____)       ||-----||      ((___)     ((___)
''',
r""" boy and girl have grown children and have earned that "middle-age spread"...
                                            |":::\
      /```|      .@@@@@,         ,,,,       66 :::|
     |` 66|_     @@@@@@@@,      @@@@@@,    (_   ':D
     C     _)    aa`@@@@@@      aa @@@@,    |_,  /
(\/)  \ ._|     (_   ?@@@@     (_  ?@@@@     \__(
 \/    ) /       =' @@@@"       =' @@@@"     //`\\     @@@@
      /`\\        \_(```         ) @@@"     | | ||    ee "@@
     /| |Y|       /``\          /-'@@@,     | |_||   (_   `D
    | | |#|      / | ||        / / \@@@     | | ||    |_  /
    | | | #\     \ | ||        \ | |@@@     | | ||     \_(
    | | |  #|    / | ||         || |@@"     |-| |<     /  \
    :=| |===:   /  | | \        || |@"      ||(((|     | ||
    | |_|, /    |  |_|  \       ||=|\       ||_:_/     | ||
     \)))||     |  (((   |      |((( \       || |      | ||
  |~~~`-`~~~|    \~~~~~~~|      |____/       || |      |_||
  |         |     \     /        || /        (( |      | `W
  |_________|      ((  |         (( |        || |      || |
  |_________|      ||  |         || |        || |      || |
      | ||         ||  |         || |        ||=|      || |
      |_||__       ||__|         //^)      __||_|     _||_|
      (____))    ((____)        ((_/Y     ((_____)   ((____)
""",
r"""boy and girl alone again
     8                            8
     8      /```|     .@@@@@,     8
     8     |  66|_    @@@@@@@@,   8 (\/)    boy and girl alone again
     8     C     _)   aa`@@@@@@   8  \/
     8(\/)  \ ._|    (_   ?@@@@   8
    |8:\/:~:~) /:~:~: =' @@@@~:~:~8
    |8::::::/\\/`\;_:::\ (__::::::8
    |8:::::| \ '|___/` \\// `\):::8
    |8::::|| | '|::/ /  ^^  \ \:::8
    |8::::|| | ' \:| \__/\__/ |:::8
    |8o:::|\ \  ' |:\_\    /_/::::8o
    |"8o:::=\ \===::/`\`%%`/'\::::"8o
    |\"8o~|  \_\  \|   `""`   |:~:~\8o
    \ \"8o\   )))  \           \::::"8o
     \ \"8o\`.  \   \           \::::"8o
      \|~~~~~| -|| -|mmmmmmmmmmmm~~~~~|
       `~~~~~|  ||  |~~|  |~|  |~~~~~~
             |  ||  |  |__| |__|
             |  ||  |  \  | \  |
             |__||__|  (~~^\(~~^\
             (   \   \  `-._)`-._)
              `-._)-._)
"""
]

if __name__ == '__main__':
    movie={'name':'love story',
            'stop':3,
            'inter':0.25,
            'frames':frames}
    # movies={'love_story':movie}

    np.save('data/movies/love_story.npy',movie)
