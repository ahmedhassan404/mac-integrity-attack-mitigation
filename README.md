# MAC Forgery and Length Extension Attack – Demonstration and Mitigation

This project explores the dangers of insecure Message Authentication Code (MAC) implementations by demonstrating a **length extension attack**. It compares an insecure server using MD5 with a secure implementation using HMAC-SHA256.

---

## Overview

The repository contains:

- An **insecure server** vulnerable to MAC forgery.
- A **secure server** that resists length extension attacks.
- Client scripts that attempt to exploit or validate the MAC logic.

---

## Directory Structure

```
mac-integrity-attack-mitigation/
├── client.py          # Attack script targeting the insecure server
├── client_mitg.py     # Attack script targeting the secure server (expected to fail)
├── server.py          # Insecure server using naive MD5-based MAC
├── server_mitg.py     # Secure server using HMAC with SHA-256
├── README.md          # Project documentation
```

---

## Getting Started

1. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   ```

2. **Activate the environment:**

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install required dependencies:**

   ```bash
   pip install hashpumpy
   ```

---

## Components

### `server.py`  
Demonstrates an insecure MAC construction using:

```python
hashlib.md5(SECRET_KEY + message)
```

This is vulnerable to length extension attacks because MD5 processes input in blocks and exposes internal state.

### `client.py`  
Uses the `hashpumpy` library to perform a length extension attack on `server.py`, successfully forging a valid MAC for a modified message.

### `server_mitg.py`  
Implements a secure MAC using:

```python
hmac.new(SECRET_KEY, message, hashlib.sha256)
```

This HMAC-based approach ensures the MAC is safe from length extension and similar attacks.

### `client_mitg.py`  
Attempts the same attack on the secure server. The forged message fails verification, demonstrating HMAC's resistance to this class of attacks.

---

## How It Works

- **Vulnerable Path**:  
  `server.py` signs a message using `md5(secret + message)`.  
  `client.py` uses `hashpumpy` to forge a new message with a valid MAC, without knowing the secret.

- **Secure Path**:  
  `server_mitg.py` uses `hmac.new()` with SHA-256, which incorporates the key securely and prevents forgery.  
  `client_mitg.py` cannot bypass this, proving the strength of the HMAC construction.

---

## Security Concepts

- **Message Authentication Code (MAC)**: A checksum used to verify data integrity and authenticity.
- **Length Extension Attack**: A cryptographic attack that targets hash functions like MD5 or SHA1 when used improperly (e.g., `hash(secret + message)`).
- **HMAC**: A secure method of keying hash functions to avoid length extension and other vulnerabilities.

---

## Best Practices

- Never concatenate a secret with a message and hash the result directly.
- Always use the `hmac` module for MACs.
- Avoid using insecure hash functions like MD5 or SHA1 for cryptographic purposes.

---

## License

This code is provided for educational purposes only. Do not use vulnerable constructions in production systems.
