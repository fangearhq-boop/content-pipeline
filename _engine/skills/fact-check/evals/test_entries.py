# Test entries with KNOWN errors for evaluating the fact-check skill.
# 10 entries: 5 correct, 3 with date/stat errors, 2 fabricated.

test_entries = [
    # 0 - CORRECT: Hank Aaron's 715th HR
    {
        "category": "On This Day", "subcategory": "Milestone",
        "month": 4, "day": 8, "year": 1974,
        "title": "Hank Aaron Breaks Babe Ruth's Home Run Record",
        "content": "Hank Aaron hit his 715th career home run off Al Downing of the Los Angeles Dodgers, surpassing Babe Ruth's long-standing record of 714. The historic blast came at Atlanta-Fulton County Stadium before 53,775 fans.",
        "source": "Baseball Reference", "difficulty": "Easy",
        "tags": "Hank Aaron, Atlanta Braves, home run record, Babe Ruth",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 1 - ERROR (wrong year): Wilt's 100-point game was 1962, not 1963
    {
        "category": "On This Day", "subcategory": "Record",
        "month": 3, "day": 2, "year": 1963,
        "title": "Wilt Chamberlain Scores 100 Points in Single Game",
        "content": "Wilt Chamberlain scored 100 points for the Philadelphia Warriors against the New York Knicks in Hershey, Pennsylvania. The game ended 169-147 and remains the single-game scoring record in NBA history.",
        "source": "Basketball Reference", "difficulty": "Easy",
        "tags": "Wilt Chamberlain, Philadelphia Warriors, scoring record",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 2 - CORRECT: Jackie Robinson's debut
    {
        "category": "On This Day", "subcategory": "Debut",
        "month": 4, "day": 15, "year": 1947,
        "title": "Jackie Robinson Breaks Baseball's Color Barrier",
        "content": "Jackie Robinson took the field for the Brooklyn Dodgers at Ebbets Field, becoming the first Black player in Major League Baseball's modern era. Robinson went 0-for-3 but scored the winning run in a 5-3 victory over the Boston Braves.",
        "source": "Baseball Reference", "difficulty": "Easy",
        "tags": "Jackie Robinson, Brooklyn Dodgers, color barrier, civil rights",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 3 - ERROR (wrong opponent): Kobe's 81 was against Raptors, not Celtics
    {
        "category": "On This Day", "subcategory": "Record",
        "month": 1, "day": 22, "year": 2006,
        "title": "Kobe Bryant Drops 81 Points Against the Celtics",
        "content": "Kobe Bryant put up 81 points against the Boston Celtics at Staples Center, the second-highest single-game total in NBA history behind Wilt Chamberlain's 100. Bryant shot 28-of-46 from the field in the Lakers' 122-104 victory.",
        "source": "Basketball Reference", "difficulty": "Easy",
        "tags": "Kobe Bryant, Los Angeles Lakers, scoring record, 81 points",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 4 - CORRECT: Bird vs Magic 1979 NCAA final
    {
        "category": "Legendary Games", "subcategory": "College",
        "month": 3, "day": 26, "year": 1979,
        "title": "Bird vs Magic NCAA Championship Game Captivates Nation",
        "content": "Magic Johnson's Michigan State Spartans defeated Larry Bird's Indiana State Sycamores 75-64 in the NCAA championship game. The matchup drew the highest TV ratings in college basketball history and launched both players into superstardom.",
        "source": "NCAA.com", "difficulty": "Medium",
        "tags": "Magic Johnson, Larry Bird, NCAA championship, Michigan State, Indiana State",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 5 - FABRICATED: Derek Jeter never hit for the cycle on this date
    {
        "category": "On This Day", "subcategory": "Record",
        "month": 7, "day": 15, "year": 2004,
        "title": "Derek Jeter Hits for the Cycle Against Red Sox",
        "content": "Derek Jeter completed the rare feat of hitting for the cycle against the Boston Red Sox at Fenway Park. Jeter went 4-for-5 with a single, double, triple, and home run as the Yankees won 11-3 in a heated rivalry matchup.",
        "source": "Baseball Reference", "difficulty": "Medium",
        "tags": "Derek Jeter, New York Yankees, hitting for the cycle, Boston Red Sox",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 6 - CORRECT: Michael Jordan's flu game
    {
        "category": "Legendary Games", "subcategory": "Playoffs",
        "month": 6, "day": 11, "year": 1997,
        "title": "Michael Jordan's Legendary Flu Game in NBA Finals",
        "content": "A visibly ill Michael Jordan scored 38 points to lead the Chicago Bulls to a 90-88 victory over the Utah Jazz in Game 5 of the NBA Finals. Jordan had to be helped off the court by Scottie Pippen after the game.",
        "source": "Basketball Reference", "difficulty": "Easy",
        "tags": "Michael Jordan, Chicago Bulls, Utah Jazz, NBA Finals, flu game",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 7 - ERROR (wrong stat): Cal Ripken's streak was 2,632, not 2,131
    {
        "category": "Record Book", "subcategory": "Streak",
        "month": 9, "day": 6, "year": 1995,
        "title": "Cal Ripken Jr Breaks Lou Gehrig's Consecutive Games Record",
        "content": "Cal Ripken Jr. played in his 2,131st consecutive game, breaking Lou Gehrig's legendary record that had stood since 1939. Ripken would eventually extend the streak to 2,500 consecutive games before voluntarily ending it in 1998.",
        "source": "Baseball Reference", "difficulty": "Easy",
        "tags": "Cal Ripken Jr, Baltimore Orioles, consecutive games, Lou Gehrig",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 8 - CORRECT: LeBron passes Kareem
    {
        "category": "On This Day", "subcategory": "Milestone",
        "month": 2, "day": 7, "year": 2023,
        "title": "LeBron James Becomes NBA's All-Time Leading Scorer",
        "content": "LeBron James passed Kareem Abdul-Jabbar to become the NBA's all-time leading scorer with a fadeaway jumper in the third quarter against the Oklahoma City Thunder. James finished the night with 38 points, pushing his career total past 38,387.",
        "source": "Basketball Reference", "difficulty": "Easy",
        "tags": "LeBron James, Los Angeles Lakers, scoring record, Kareem Abdul-Jabbar",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
    # 9 - FABRICATED: Tim Duncan was never traded to the Lakers
    {
        "category": "Traded Away Too Soon", "subcategory": "Trade",
        "month": 8, "day": 12, "year": 2003,
        "title": "Spurs Trade Tim Duncan to Lakers in Blockbuster Deal",
        "content": "The San Antonio Spurs shocked the basketball world by trading Tim Duncan to the Los Angeles Lakers in exchange for Shaquille O'Neal and two first-round picks. The trade reshaped the Western Conference for the next decade.",
        "source": "Basketball Reference", "difficulty": "Hard",
        "tags": "Tim Duncan, San Antonio Spurs, Los Angeles Lakers, Shaquille O'Neal, trade",
        "last_used": None, "use_count": 0, "record_status": "Active",
        "verified_through": "2026-02-24"
    },
]
