import requests
from datetime import datetime

url = 'http://172.24.16.128:8889/nlu_engine?agent_id=1199'


def time_difference_in_ms(date1, date2):
    if isinstance(date1, str):
        date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    if isinstance(date2, str):
        date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

    time_diff = date2 - date1

    time_diff_ms = time_diff.total_seconds() * 1000

    return int(time_diff_ms)


data = [
    # "hey baby oh man i missed you i'm gonna try and call you back again i'm gonna call my daughters though listen are you watering my plants by any chance i hope you are they're probably dry as can be i'm doing okay i've been working out day 4 today just because i'm starting to gain some weight and i don't really like it i mean it's it's healthier looking but still i am gonna do iop i'll on the on the computer and i still really wanna come home  but if not i'm thinking about ocala too but i really wanna come home   alright baby i love you i hope you're doing okay i'm thinking of you i'm gonna try and call you back right after this again i hope you answer alright talk to you later hope you're feeling better bye bye",
    # "hey berg it's amy please call me i have somebody that can run the",
    "hey bev just pulled into the storage unit did you get here and leave or did you just not get here at all  well whatever the case may be i'm here now and  well i'm gonna do my best hopefully i don't drop the bike and him on his head later",
    "hey bitch made you left my house with the door wide open and then you didn't even help me pick this no shit up off the ground that you didn't take the fucking trash out for don't come back to my house  nothing but to pick up your motherfucking call because you gonna have on the inside of my fucking house i'm gonna cut your shit up right fucking now",
    "hey bobby your message sucks",
    "hey brandon this is anya give me a call",
    "hey burke it's amy i'm finally back in the office i'd love to talk to you if you could give me a call that would be fantastic have a great day",
    # "hey cara hello i just don't know",
    # "hey chico chip smith it's about 5 20 sorry i didn't get back to you sooner but if you could please call me 7 1 3 8 8 4 7 6 7 6 thank",
    # "hey chris hulbert here and i'm thrilled to hear something truly special with you as many of you know it's dick bigger strategy is the brain child of the late fx chief it is a genuine masterpiece in the world of forex trading so i am deeply honored to have the opportunity to contribute and refine this incredible strategy elevated it's a new heights and potential so tonight at 7 p.m. we will on veil the strategy and we will embark on transformative journey together i invite you to join us as we unveiled a full capabilities of the strategy optimize and enhance for maximum performance so let's unlock new levels of success together go ahead and check your email for the special invite and seats are limited i'll see you soon",
    "hey chris this is harsh i'm calling from expedios i got your profile from 1 of the job boards and wanted to discuss the exciting opportunity of district manager which is in punta gorda florida  for a very good company of storage facilities if you're interested please call back on this number which is 3 0 2 4 7 1 8 7 2 8 i'm looking forward to talking with you thank you and have a great day that's all",
    "hey cole bring back my fucking tools  shit without asking still little fucker looking all over the place for my stuff bring it back all of it",
    # "hey cooper pending phone number +877-209-400-6328 regarding television just a matter working press 2 now to reserve a night",
    # "hey daddy call me back please",
    # "hey danny trying to reach michael",
    # "hey david it's bryce at fundera i just spoke to sun i believe and he told me to give you a call just got some updates on your application and i wanted to yeah touch base over that looks like we're getting some final options today have a few questions to clarify a few things and we'll be set to go so give me a callback when you chance thanks bye",
    # "hey derek this is bob millette just wondering when you're gonna come down and get mower finished up for me thank you",
    # "hey derek this is dave spirock here on margaret street in niles and went out to cut the grass a few minutes ago in that tractor ran for about 5 minutes and it started kinda surging like it was running out of gas but it's got 3 quarters tank of gas then i shut it down to pick up some debris out of the yard and i can't get it started again so i thought i'd give you a call i know you worked on it here just and i've only had it out once since you were here last this is the second time so can give me a call number 2 6 9 2 4 0 8 5 9 3 thank you and have a great afternoon",
    # "hey dog give me a call",
    # "hey don this is reggie i missed your call call me back",
    # "hey dylan it's just me your just a normal friend sam and i just wanna say is sorry if actually a nightmare sorry i just wanted to let you know it's we're gonna have a court meeting judge later on so i hope you could answer your phone soon dylan and you don't want to be invited brenda to the judge right",
    # "hey ed it's stacy edwards i'm calling from activate center today is monday my phone number is 8 8 8 3 3 7 8 9 5 3 and our file shows that you've got some back taxes still due i wanted to let  know that you can enroll to have them eliminated with the new 0 tax program so any small or large amount are now noncollectible through this program but you have to enroll so give me a callback and we can get you all  it's not gonna take too long it's really a 1 and done setup so i'll keep the account open through the end of the week so again my number is 8 8 8 3 3 7 8 9 5 3 thanks",
    "hey ed stacy edwards i'm calling from activate center today is tuesday my phone number is 8 8 8 3 3 7 8 9 5 3 and our file shows that you've got some back taxes still due  i wanted to let you know that you can enroll to have them eliminated with the new 0 tax program so any small or large amount are now noncollectible through this program but you have to enroll so give me a callback and we can get you all set up it's not gonna take too long it's really a 1 and done setup so i'll keep the account open through the end of the week so again my number is 8 8 8 3 3 7 8 9 5 3 thanks",
    "hey emily this is andrew with housecall pro i wanted to reach out and chat about your account give me a callback when you get a chance i'm at 9 7 0 7 7 1 7 7 3 6 again that's 9 7 0 7 7 1 7 7 3 6 so much talk to you soon",
    # "hey ferguson it's amy give me a call",
    # "hey give me a call give me a call since you get this message kenny",
    # "hey give me a call when you get this bill i need to talk to you whatever send it that way",
    "hey give me a callback when you get this",
    "hey good afternoon enrique it's hi enrique it's me ron from gosek",
    # "hey good day this rod with insure dot hello",
    # "hey good morning this is margaret good morning this is margaret robbie from western new york medical i'm calling for scott",
    # "hey google yes could they answer",
    "hey has christopher calling  ai assistant"
]

# intents = ['scammers', 'spam', 'action', 'question', 'who_calling', 'important', 'confirmation',
#            'bad_connection', 'repeat', 'null', 'thank_you', 'abuse', 'congrats', 'call_reason', 'bye']

intents = ['abc']

# entities = ['abc']

entities = ['name']

print(','.join(['phrase_length', 'delay_1',
                # 'delay_2', 'delay_3', 'delay_4', 'delay_5', 'delay_6', 'delay_7',
                # 'delay_8', 'delay_9', 'delay_10', 'delay_11', 'delay_12', 'delay_13', 'delay_14', 'delay_15'
                ]))

total_results = []

for phrase in data:
    x = 0
    phrase_results = [str(len(phrase))]
    while x < len(intents):
        x = x + 1
        body = {
            "language": "en-US",
            "utterance": phrase,
            "context": "date_default",
            "use_neuro_api": False,
            "use_synonyms": False,
            "entities": entities,
            # "intents": intents[0:x],
            "intents": intents,
            "entities_policy": 1,
            "intents_policy": 1,
            "session_uuid": "d9de21bd-6288-483c-918e-d0fda969c470",
            "asr_params": {
                "deepgram_model": "nova-2-phonecall"
            },
            "asr_engine": "deepgram"
        }

        average = []
        for i in range(50):
            before = datetime.now()
            response = requests.post(url, json=body)
            after = datetime.now()

            if response.status_code == 200:
                average.append(str(time_difference_in_ms(before, after)))
            else:
                average.append('E')

        total_delay = 0
        counter = 0
        for item in average:
            if int(item):
                total_delay = total_delay + int(item)
                counter = counter + 1

        phrase_results.append(str(round(total_delay / counter)))

    print(','.join(phrase_results))
