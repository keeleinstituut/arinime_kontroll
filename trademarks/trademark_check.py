import utils.trademark_processing as tp


def et_trademark_check(bis_name, bis_domain):
    result = True
    message = 'Kaubamärgi konflikti ei tekki'
    tp.init_tm()
    et_trademarks = tp.get_tm_names()
    tms = [x['tm'] for x in et_trademarks]
    cls = [x['class'] for x in et_trademarks]

    tms = list(map(lambda x: str(x).lower(), tms))
    
    if bis_name.lower() in tms:
        if bis_domain in cls[tms.index(bis_name)]:
            result = False
            message = 'Valitud tegevusalal on kaubamärk kaitstud'

    return result, message
