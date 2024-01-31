def multiple_returns(sentence):
	if not sentence:
		sentence = None
	if sentence:
		sen_len = len(sentence)
	return (sen_len, sentence if not sentence else sentence[:1])
