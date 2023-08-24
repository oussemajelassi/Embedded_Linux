SUMMARY = "A customized image for development purposes."
LICENSE = "MIT"
inherit core-image
IMAGE_FEATURES += "splash"
IMAGE_FEATURES += "tools-debug"
IMAGE_FEATURES += "tools-profile"
IMAGE_FEATURES += "tools-sdk"
IMAGE_FEATURES += "ssh-server-dropbear"
IMAGE_INSTALL:append = " mc"
IMAGE_INSTALL:append = " nano"
IMAGE_INSTALL:remove = "dropbear"

IMAGE_INSTALL +="libmodbus"
IMAGE_INSTALL +="application"
IMAGE_INTSALL +="staticIP"


