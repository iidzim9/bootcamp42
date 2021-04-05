# import string
class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        sum = 0
        for q, w in zip(coefs, words):
            sum += q * len(w)
        return sum

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(words) != len(coefs):
            return -1
        sum = 0
        for cpt, w in enumerate(words, 0):
           sum += coefs[cpt] * len(w)
        return sum

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
