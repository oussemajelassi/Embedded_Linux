SUMMARY = "Script to start Modbus application slave"
SECTION = "custom"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302" 

SRC_URI  = "file://application"

inherit update-rc.d

INITSCRIPT_NAME = "application"

do_install() {
  install -d ${D}${sysconfdir}
  install -d ${D}${sysconfdir}/init.d
  install -m 755 ${WORKDIR}/application ${D}${sysconfdir}/init.d/application
}
