def reverse(text):
   chars = list(text)
   output = ''
   ch_len = len(chars)
   while ch_len > 0 :
       output = output+chars[ch_len-1]
       ch_len -= 1
   return output
