#UFuscator (Fast, Reliable and Open-Source)
import lzma, base64, sys, random

mental = '_' + ''.join(random.choice('01') for _ in range(50))

if len(sys.argv) > 2:
    with open(sys.argv[1], 'r') as file:
        python_code = file.read()
        final_code = f"#Obfuscated by UFuscator\nimport lzma, base64;{mental} = [int('{''.join(format(byte, '08b') for byte in lzma.compress(base64.b64encode(python_code.encode())))}'[i:i+8], 2) for i in range(0, len('{''.join(format(byte, '08b') for byte in lzma.compress(base64.b64encode(python_code.encode())))}'), 8)];exec(base64.b64decode(lzma.decompress(bytes({mental}))))"
        for i in range(int(sys.argv[2])):
            final_code = f"#Obfuscated by UFuscator\nimport lzma, base64;{mental} = [int('{''.join(format(byte, '08b') for byte in lzma.compress(base64.b64encode(final_code.encode())))}'[i:i+8], 2) for i in range(0, len('{''.join(format(byte, '08b') for byte in lzma.compress(base64.b64encode(final_code.encode())))}'), 8)];exec(base64.b64decode(lzma.decompress(bytes({mental}))))"
        with open(f"obfuscated_{sys.argv[1]}", 'w') as file:
            file.write(final_code)
else:
    print("Usage:\npython3 UFuscator.py [File Name/Path] [Obfuscator loop]\n\nexample: python3 UFuscator.py test.py 10\n\nObfuscated 10 times file called test.py")
