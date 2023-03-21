CryptoSystems

Affine Cipher:

The Affine uses modulo arithmetic to perform a calculation on the numerical value of a letter to create encrypted message.Each letter is converted to it's decimal representation and mapped into another number and converted back to a letter.
it's encrypted with the formula: (ax +  b) mod m
where a and b are numbers between 0 and m, and a is relatively prime with m. m in our case is 26(length of the alphabet).
To encrypt back (decrypt) we need to fine the multiplicatve inverse of a mod m. If a and m are relatively prime the multiplicative inverse is unique, which guarantees us to find our original text.

The way our code is implemented:

we don't need to create objects as the class methods are static type.
to encrypt with Affine cipher we just need to call the class name followed by the encrypt method.(Affine.encrypt(message,[a,b]))
The encrypt method takes two positional arguments ( they are required )
The first argument is the message to be encrypted, the second one is a key in the form of [a,b] where a and b are less than 26 and greater than zero, and a is relatively prime with 26.
To decrypt we need to call the class Affine followed by the decrypt method.
(Affine.decrypt(message,[a,b])) the key has to be similar with one we encrypted the data with.

Transposition Cipher:

is a crypto system where the order of the alphabets in the plain text is rearranged to for a cipher text. It does this without changing the alphabets, it only changes the permutation of the words. This is an ancient crypto system used for many years but is unreliable. There are many ways to create the permutaion of the letters. The one we implemented creates blocks and shuffles each block.

The way our code is implementd:

No need to create objects.
To encrypt: we need to call the class Transposition followed by the encrypt method.
(Transpotion.encrypt(message,[key]))

Description of key: [key] takes each value of the block from their index to the index specified by the number in the key with the same index.
example: [3,1,2,4]
this means take the first letter in the block to the third position.
		the second letter to the first position.
		the third letter to the second, and leave the last one as it is
this is done in the same way in every block.

To decrypt call the class followed by the method decrypt
( Transpostion.decrypt(message,[key])),the key has to be similar with one we encrypted the data with.


RSA:

Named after the founders (Rivest  - Shamir - Adleman) is a public key cryptosystem which is is used widely. It's a public-key cryptosystem. The main notion behind RSA encryption algorithm is that it's hard to factorize a large integer.
RSA is an asymmetric algorithm meaning it uses two different keys namely public key and private key.

The way our code is implemeted:

as the other systems we don't need to create objects.
Call the class name followed by the encrypt method.
(RSA.encrypt(message,[key]))
to encrypt we should first call RSA.genenatekey(P,Q) and pass to prime numbers. this method returns two list of numbers, publickey and private key we need to store them in separate variable so that we can decrypt them.

so the key in the encrtypt method is the public key.

to decrypt back we just need to pass the value of private key to the RSA.decrypt() function.



Section 1 

Group Members:

1.Amanuel Yihune -- UGR/8408/13
2.Nathnael Yimer -- UGR/6855/13
3.Zelalem Habtamu -- UGR/7301/13
4.Yonas Engdu -- UGR/4575/13
5.Abdi Firomsa -- UGR/8420/13


