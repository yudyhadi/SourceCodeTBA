import streamlit as st
import string

st.write("""
# Parser dan Lexical Analyzer
 Penganalisis leksikal mbedakake sintaksis kasebut dadi seri token, kanthi ngilangi spasi putih utawa komentar ing kode sumber. Tabel Parse bisa ngarujuk marang versi sing didhukung tabel saka: Parser LR nggunakake tabel sing asale saka grammar dening generator parser. Parser LL nggunakake tabel sing asale saka grammar.
""")
st.write('Contoh : Aku Kampleng Gendul')
st.write('SU (Subjek) : Aku, Kowe')
st.write('PR (Predikat) :  Kampleng, Klebu, Waca, Wegah')
st.write('OB (Objek) : Pupu, Udik, Gendul, Wayang')
sentence = st.text_input("Masukkan Kalimat : ", placeholder="Masukkan kalimat dengan format SU PR OB")
validasi = st.button("Validasi")

input_string = sentence.lower()+'#'
tokens = sentence.lower().split()
tokens.append('EOS')

# inisialisasi
alphabet_list = list(string.ascii_lowercase)
state_list = ["q0","q1","q2","q3","q4","q5","q6","q7","q8","q9","q10",
    "q11","q12","q13","q14","q15","q16","q17","q18","q19","q20",
    "q21","q22","q23","q24","q25","q26","q27","q28","q29","q30",
    "q31","q32"]

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

# spasi sebelum input
transition_table['q0', ' '] = 'q0'

transition_table[('q0', 'p')] = 'q1'
transition_table[('q0', 'a')] = 'q4'
transition_table[('q0', 'u')] = 'q5'
transition_table[('q0', 'k')] = 'q8'
transition_table[('q0', 'w')] = 'q20'
transition_table[('q0', 'g')] = 'q27'
transition_table[('q1', 'u')] = 'q2'
transition_table[('q2', 'p')] = 'q3'
transition_table[('q3', 'u')] = 'q32'
transition_table[('q4', 'k')] = 'q3'
transition_table[('q5', 'd')] = 'q6'
transition_table[('q6', 'i')] = 'q7'
transition_table[('q7', 'k')] = 'q32'
transition_table[('q8', 'l')] = 'q9'
transition_table[('q8', 'o')] = 'q12'
transition_table[('q8', 'a')] = 'q14'
transition_table[('q9', 'e')] = 'q10'
transition_table[('q10', 'b')] = 'q11'
transition_table[('q11', 'u')] = 'q32'
transition_table[('q12', 'w')] = 'q13'
transition_table[('q13', 'e')] = 'q32'
transition_table[('q14', 'm')] = 'q15'
transition_table[('q15', 'p')] = 'q16'
transition_table[('q16', 'l')] = 'q17'
transition_table[('q17', 'e')] = 'q18'
transition_table[('q18', 'n')] = 'q19'
transition_table[('q19', 'g')] = 'q32'
transition_table[('q20', 'a')] = 'q21'
transition_table[('q20', 'e')] = 'q24'
transition_table[('q21', 'y')] = 'q22'
transition_table[('q21', 'c')] = 'q23'
transition_table[('q22', 'a')] = 'q18'
transition_table[('q23', 'a')] = 'q32'
transition_table[('q24', 'g')] = 'q25'
transition_table[('q25', 'a')] = 'q26'
transition_table[('q26', 'h')] = 'q32'
transition_table[('q27', 'e')] = 'q28'
transition_table[('q28', 'n')] = 'q29'
transition_table[('q29', 'd')] = 'q30'
transition_table[('q30', 'u')] = 'q31'
transition_table[('q31', 'l')] = 'q32'
transition_table[('q32', ' ')] = 'q32'
transition_table[('q32', 'p')] = 'q1'
transition_table[('q32', 'a')] = 'q4'
transition_table[('q32', 'u')] = 'q5'
transition_table[('q32', 'k')] = 'q8'
transition_table[('q32', 'w')] = 'q20'
transition_table[('q32', 'g')] = 'q27'
transition_table[('q32', '#')] = 'accept'

# definition untuk simbol non-terminal dan simbol terminal
non_terminal = ['S', 'SU', 'PR', 'OB']
terminals = ['aku', 'kowe', 'kampleng', 'klebu', 'waca', 'wegah', 'pupu', 'udik', 'gendul', 'wayang']

# definition untuk parse table
parse_table = {}

parse_table[('S', 'aku')] = ['SU', 'PR', 'OB']
parse_table[('S', 'kowe')] = ['SU', 'PR', 'OB']
parse_table[('S', 'kampleng')] = ['error']
parse_table[('S', 'klebu')] = ['error']
parse_table[('S', 'waca')] = ['error']
parse_table[('S', 'wegah')] = ['error']
parse_table[('S', 'pupu')] = ['error']
parse_table[('S', 'udik')] = ['error']
parse_table[('S', 'gendul')] = ['error']
parse_table[('S', 'wayang')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('SU', 'aku')] = ['aku']
parse_table[('SU', 'kowe')] = ['kowe']
parse_table[('SU', 'kampleng')] = ['error']
parse_table[('SU', 'klebu')] = ['error']
parse_table[('SU', 'waca')] = ['error']
parse_table[('SU', 'wegah')] = ['error']
parse_table[('SU', 'pupu')] = ['error']
parse_table[('SU', 'udik')] = ['error']
parse_table[('SU', 'gendul')] = ['error']
parse_table[('SU', 'wayang')] = ['error']
parse_table[('SU', 'EOS')] = ['error']


parse_table[('PR', 'aku')] = ['error']
parse_table[('PR', 'kowe')] = ['error']
parse_table[('PR', 'kampleng')] = ['kampleng']
parse_table[('PR', 'klebu')] = ['klebu']
parse_table[('PR', 'waca')] = ['waca']
parse_table[('PR', 'wegah')] = ['wegah']
parse_table[('PR', 'pupu')] = ['error']
parse_table[('PR', 'udik')] = ['error']
parse_table[('PR', 'gendul')] = ['error']
parse_table[('PR', 'wayang')] = ['error']
parse_table[('PR', 'EOS')] = ['error']

parse_table[('OB', 'aku')] = ['error']
parse_table[('OB', 'kowe')] = ['error']
parse_table[('OB', 'kampleng')] = ['error']
parse_table[('OB', 'klebu')] = ['error']
parse_table[('OB', 'waca')] = ['error']
parse_table[('OB', 'wegah')] = ['error']
parse_table[('OB', 'pupu')] = ['pupu']
parse_table[('OB', 'udik')] = ['udik']
parse_table[('OB', 'gendul')] = ['gendul']
parse_table[('OB', 'wayang')] = ['wayang']
parse_table[('OB', 'EOS')] = ['accept']


# lexical analyzer main program
if validasi:
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q32':
            st.write('current token: ', current_token, ', valid')
            current_token = ''
        if state == 'error':
            st.write('error')
            break
        idx_char = idx_char + 1

    # conclusion
    if state == 'accept':
        st.write('Semua token di input : ', sentence, ', valid')

    # parser main program

    # Stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    # Input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    # parsing
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        st.write('top= ', top)
        st.write('symbol= ', symbol)
        if top in terminals:
            st.write('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_token = idx_token+1
                symbol = tokens[idx_token]
                if symbol == 'EOS':
                    st.write('isi stack: ', str(stack))
                    stack.pop()
            else:
                st.write('error')
                break
        elif top in non_terminal:
            st.write('top adalah symbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbols_to_be_paused = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_paused)-1, -1, -1):
                    stack.append(symbols_to_be_paused[i])
            else:
                st.write('error')
                break
        else:
            st.write('error')
            break
        st.write('isi stack:', str(stack))
        st.markdown("""---""")

    # conclusion
    st.write()
    if symbol == 'EOS' and len(stack) == 0:
        st.success('input string: '+sentence+' valid, sesuai Grammar')
        st.spinner('Please wait...')
        st.snow()
    else:
        st.error('Error, input string '+sentence+' invalid, tidak sesuai dengan Grammar')