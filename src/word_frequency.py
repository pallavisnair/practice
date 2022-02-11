def clean_text(text, punctuations):
    replaced = text
    punctuations1 = list(punctuations)
    for p in punctuations1:
        replaced = replaced.replace(p, "")
    return replaced

def is_valid(word):
    return word.isalpha()

def word_cloud(input_message, avoid, punctuations):
    new_input = clean_text(input_message.lower(), punctuations).split()
    output_message = {}
    for word in new_input:
        if word not in avoid:
            if is_valid(word):
                output_message[word] = output_message.get(word, 0) + 1
    return output_message


