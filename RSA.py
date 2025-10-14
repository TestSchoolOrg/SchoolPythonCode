alf = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

pre = []

word = list(input("Введите слово: "))
formatted_word = "".join(word)
print(f"Изначальное слово: {formatted_word}")

for i in range(len(word)):
    u = alf.index(word[i]) + 1
    y = u ** 7
    o = y % 33
    pre.append(alf[o])

result = "".join(pre)
print(f"Зашифрованное слово: {result}")
