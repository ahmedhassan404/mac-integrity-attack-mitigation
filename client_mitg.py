import server_mitg  # Assuming server.py has the 'verify' function

def perform_attack():
    # Step 1: Intercepted values from the server
    intercepted_message = b"amount=100&to=alice"   # Original message intercepted
    intercepted_mac = "a86f897948d15c923c1f77133e805c707ca4fa752e3960efde47d618425027d5"  # Original MAC from server_mitg.py output

    # Step 2: Malicious data to append
    data_to_append = b"&admin=true"  # Attack data

    # Step 3: Key length (this should match the secret key length used in the server)
    key_length = 14  # Adjust based on the server's secret key length

    # Step 4: Perform length extension attack using hashpumpy
    result = hashpumpy.hashpump(intercepted_mac, intercepted_message, data_to_append, key_length)
    forged_mac = result[0]
    forged_message = result[1]  # Already bytes, no need to encode

    # Step 5: Extract forged MAC and message
  
    # Print forged message and MAC
    print("=== Attacker Simulation ===")
    print("Forged message:", forged_message)
    print("Forged MAC:", forged_mac)

    # Step 6: Use server's verify function to check if the forged MAC is valid
    if server_mitg.verify(forged_message, forged_mac):
        print("MAC verified successfully (attack succeeded!)")
    else:
        print("MAC verification failed (attack failed)")

if __name__ == "__main__":
    perform_attack()