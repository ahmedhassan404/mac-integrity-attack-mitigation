#client
import hashpumpy
import server  # Assuming server.py has the 'verify' function

def perform_attack():
    # Step 1: Intercepted values from the server
    intercepted_message = b"amount=100&to=alice"   # Original message intercepted
    intercepted_mac = "614d28d808af46d3702fe35fae67267c"  # Original MAC from server.py output

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
    if server.verify(forged_message, forged_mac):
        print("MAC verified successfully (attack succeeded!)")
    else:
        print("MAC verification failed (attack failed)")

if __name__ == "__main__":
    perform_attack()