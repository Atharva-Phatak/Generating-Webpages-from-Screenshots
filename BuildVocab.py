#The utility functions will to map the DSL vocabulary to Bootstrap - HTML tokens

def load_file(Fname):
    
    file = open(Fname , 'r')
    text = file.read()
    file.close()
    
    return text


#Lets build a vocabulary wrapper which mapswors and ids

class Vocabulary(object):
    
    def __init__(self):
        
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0
        
    def add_word(self , word):
        
        if not word in self.word2idx:
            
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1
            
    def __call__(self  , word):
        
        if not word in self.word2idx:
            
            return self.word2idx['<unk>']
        
        return self.word2idx[word]
    
    def __len__(self):
        
        return len(self.word2idx)
    
def build_vocab(Fpath):
    
    vocab = Vocabulary()
    raw_words = load_file(Fpath)
    
    words = set(raw_words.split(' '))
    
    for i , word in enumerate(words):
        
        vocab.add_word(word)
        
    vocab.add_word(' ')
    vocab.add_word('<unk>')
    
    print("Created vocabulary of {} items".format(len(vocab)))
    return vocab
            