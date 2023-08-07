SUMMARY = " hello world custom application "
DESCRIPTION = " Custom Recipe "
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"
DEPENDS += "libmodbus"
SRC_URI = "file://src"
S = "${WORKDIR}/src"
do_compile(){
${CC} ${CFLAGS} ${LDFLAGS} application.c -o application -I/${RECIPE_SYSROOT}/${includedir}/modbus/ -lmodbus

}

do_install () {
install -d ${D}${bindir}
install -d ${D}${sysconfdir_native}
install -m 0755 application ${D}${bindir}
install -m 0644 config.txt ${D}${sysconfdir_native}
}

FILES:${PN} += "${sysconfdir_native}/config.txt"
