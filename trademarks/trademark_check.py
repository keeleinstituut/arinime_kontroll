from pydantic import conint
import utils.trademark_processing as tp


def et_trademark_check(bis_name, bis_domain):
    result = True
    message = 'Kaubamärgi konflikti ei tekki'
    tp.init_tm()
    et_trademarks = tp.get_tm_names()
    tms = [x['tm'] for x in et_trademarks]
    cls = [x['class'] for x in et_trademarks]

    tms = list(map(lambda x: str(x).lower(), tms))
    
    collect_trademarks = {}
    bis_name = bis_name.lower()

    for tm in tms:
        if bis_name in tm:
            if bis_domain in cls[tms.index(tm)]:
                collect_trademarks['kaubamärk: '+ str(tm)]='tegevusala: ' + str(cls[tms.index(tm)])
                continue

    if len(collect_trademarks) > 0:
        result = False
        message = 'Valitud tegevusalal on kaubamärk kaitstud'

    return result, message, collect_trademarks

#if __name__ == "__main__":
#    test_name = 'nublu'
#    test_dom = "25"
#    x = et_trademark_check(test_name, test_dom)