SUMMARY = " systemd Static IP adress "
DESCRIPTION = " Custom Recipe "
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"
SRC_URI = "file://src"
S = "${WORKDIR}/src"

do_install () {
install -d ${D}${systemd_unitdir}/network
install -m 00-eth0.network ${D}${systemd_unitdir}/network
}

FILES:${PN} += "${systemd_unitdir}/network/00-eth0.network"
