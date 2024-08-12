{"filter":false,"title":"caesar.py","tooltip":"/caesar.py","undoManager":{"mark":26,"position":26,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"insert","lines":["def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet"],"id":2}],[{"start":{"row":2,"column":25},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":4},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":6},{"start":{"row":3,"column":4},"end":{"row":4,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":8}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":4,"column":0},"end":{"row":6,"column":26},"action":"insert","lines":["def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt"],"id":10}],[{"start":{"row":6,"column":26},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":8,"column":0},"end":{"row":10,"column":22},"action":"insert","lines":["def getCipherKey():","    shiftAmount = input( \"Please enter a key (whole number from 1-25): \")","    return shiftAmount"],"id":13}],[{"start":{"row":10,"column":22},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":17}],[{"start":{"row":12,"column":0},"end":{"row":23,"column":27},"action":"insert","lines":["def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage"],"id":18}],[{"start":{"row":23,"column":27},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":25,"column":0},"end":{"row":27,"column":56},"action":"insert","lines":["def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)"],"id":22}],[{"start":{"row":27,"column":56},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":24}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":29,"column":0},"end":{"row":41,"column":52},"action":"insert","lines":["def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decypted Message: {myDecryptedMessage}')"],"id":26}],[{"start":{"row":41,"column":52},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]},{"start":{"row":42,"column":4},"end":{"row":43,"column":0},"action":"insert","lines":["",""]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "],"id":28}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":24},"action":"insert","lines":["runCaesarCipherProgram()"],"id":29}],[{"start":{"row":43,"column":24},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"remove","lines":["",""],"id":31},{"start":{"row":43,"column":24},"end":{"row":44,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":214,"scrollleft":0,"selection":{"start":{"row":38,"column":52},"end":{"row":38,"column":52},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1723396404360,"hash":"7483dec790cbb21a98e763834d663086edc8cbe7"}