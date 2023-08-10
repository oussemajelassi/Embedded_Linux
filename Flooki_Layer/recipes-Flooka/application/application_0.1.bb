SUMMARY = " hello world custom application "
DESCRIPTION = " Custom Recipe "
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"
inherit systemd

DEPENDS += "libmodbus"

SRC_URI = "file://myapplication.service \
	   file://src"

#S = "${WORKDIR}/src"
S = "${WORKDIR}"


SYSTEMD_SERVICE:${PN} = "myapplication.service"
SYSTEMD_AUTO_ENABLE = "enable"

do_compile(){
cd src
${CC} ${CFLAGS} ${LDFLAGS} application.c -o application -I/${RECIPE_SYSROOT}/${includedir}/modbus/ -lmodbus

}

do_install () {
install -d ${D}${bindir}
install -d ${D}${sysconfdir_native}

install -m 0755 src/application ${D}${bindir}
install -m 0644 src/config.txt ${D}${sysconfdir_native}

}
do_install:append(){
install -d ${D}/${systemd_unitdir}/system
install -m 0644 myapplication.service ${D}/${systemd_unitdir}/system
}

FILES:${PN} += "${sysconfdir_native}/config.txt"
FILES:${PN} += "${systemd_unitdir}/system/myapplication.service"
