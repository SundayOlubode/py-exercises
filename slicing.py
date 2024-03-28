word = 'X-DSPAM-Confidence:0.8475'
colpos = word.find(':')
fig = word[(colpos+1):]
fig = float(fig)
print('The extracted figure is ', fig)
