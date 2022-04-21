# Blowfish Electronic Codebook Mode (ECB)

Note: ECB mode does not provide strong confidentiality, regardless of the cipher, and is not recommended for use in applications.

To encrypt or decrypt data in ECB mode, use encrypt_ecb or decrypt_ecb methods of the Cipher object. ECB mode can only operate on data that is a multiple of the block-size in length.

# Run:

`./test10.py`

# Expected Output:


```
PASS
```

