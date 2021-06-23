# What is Intersight?

# What is UCS?

# How to setup Intersight to run your wokflows

## Claim a device

- Login to UCS - You have to have a UCS director setup or
  - Go to Admin -> Device Connector
  - Claim a device
    - Save the device ID
    - Save the device claim code
- Go to intersight.com
  - Go to your Account -> ADMIN -> Targets
    - Add a new UCS Manager Target
    - Paste the device ID and claim code that you got from UCS Manager
    - Go to the Device (click on it) -> Settings -> License and activate the trial license.
    - Generate a new API Key and Secret key. You will need these to authenticate.

TADA! You are almost there...
