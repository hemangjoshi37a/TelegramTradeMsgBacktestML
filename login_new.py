from jugaad_trader import Zerodha
import pyotp
import joblib
import zerodhaAuth

def login_haj_new():
    ######################################################
    my_user_id = zerodhaAuth.haj_my_user_id
    my_password = zerodhaAuth.haj_my_password
    my_twofa_key =zerodhaAuth.haj_my_twofa_key
    my_PIN = zerodhaAuth.haj_my_PIN
    ####################################################
    this_totp_class = pyotp.TOTP(my_twofa_key)
    this_totp_pin = this_totp_class.now()
    kite = Zerodha(user_id=my_user_id,password=my_password,twofa='498234') ## TWOFA= PIN or  this_totp_pin ##
    kite.login()
    #######################################################
    joblib.dump(kite,'kitefile.p')
    joblib.dump(kite,'../kitefile.p')
    joblib.dump(kite,'../../kitefile.p')
    joblib.dump(kite,'../../../kitefile.p')
    display(kite.profile()['user_name'])
    return kite

def login_aaj_new():
    ######################################################
    my_user_id = zerodhaAuth.aaj_my_user_id
    my_password = zerodhaAuth.aaj_my_password
    my_twofa_key =zerodhaAuth.aaj_my_twofa_key
    my_PIN = zerodhaAuth.aaj_my_PIN
    ####################################################
    this_totp_class = pyotp.TOTP(my_twofa_key)
    this_totp_pin = this_totp_class.now()
    kite = Zerodha(user_id=my_user_id,password=my_password,twofa=my_PIN) ## TWOFA= PIN or  this_totp_pin ##
    kite.login()
    ######################################################
    joblib.dump(kite,'kitefile.p')
    joblib.dump(kite,'../kitefile.p')
    joblib.dump(kite,'../../kitefile.p')
    joblib.dump(kite,'../../../kitefile.p')
    display(kite.profile()['user_name'])
    return kite
