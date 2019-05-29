Name:		wn75pkg
Version:	1.0.3
Release:	6%{?dist}
Summary:	SL75 meta-packages
Group:		Applications/Internet
License:	ASL 2.0
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       389-ds-base-devel
Requires:       389-ds-base-libs
Requires:       a2ps
Requires:       abrt
Requires:       abrt-addon-ccpp
Requires:       abrt-addon-kerneloops
Requires:       abrt-addon-python
Requires:       abrt-cli
Requires:       abrt-libs
Requires:       abrt-tui
Requires:       acl
Requires:       acpid
Requires:       aic94xx-firmware
Requires:       akonadi
Requires:       alsa-lib
Requires:       alsa-lib-devel
Requires:       alsa-utils
Requires:       ant
Requires:       antlr
Requires:       apr
Requires:       apr-devel
Requires:       apr-util
Requires:       apr-util-devel
Requires:       apr-util-ldap
Requires:       arts
Requires:       at
Requires:       atk
Requires:       atk-devel
Requires:       atlas
Requires:       attr
Requires:       audiofile
Requires:       audispd-plugins
Requires:       audit
Requires:       audit-libs
Requires:       audit-libs-devel
Requires:       augeas
Requires:       authconfig
Requires:       autoconf
Requires:       automake
Requires:       automoc
Requires:       avahi-glib
Requires:       avahi-libs
Requires:       babel
Requires:       babl
Requires:       basesystem
Requires:       bash
Requires:       bc
Requires:       bcel
Requires:       bind-libs
Requires:       bind-utils
Requires:       binutils
Requires:       binutils-devel
Requires:       biosdevname
Requires:       bison
Requires:       blas
Requires:       blktrace
Requires:       bluez-libs
Requires:       boost
Requires:       boost-date-time
Requires:       boost-devel
Requires:       boost-filesystem
Requires:       boost-graph
Requires:       boost-iostreams
Requires:       boost-program-options
Requires:       boost-python
Requires:       boost-regex
Requires:       boost-serialization
Requires:       boost-signals
Requires:       boost-system
Requires:       boost-test
Requires:       boost-thread
Requires:       boost-wave
Requires:       bouncycastle
Requires:       bridge-utils
Requires:       brltty
Requires:       byacc
Requires:       bzip2
Requires:       bzip2-devel
Requires:       bzip2-libs
Requires:       bzr
Requires:       ca-certificates
Requires:       cairo
Requires:       cairo-devel
Requires:       cairomm
Requires:       c-ares
Requires:       cdparanoia-libs
Requires:       certmonger
Requires:       CGSI-gSOAP
Requires:       check
Requires:       check-devel
Requires:       checkpolicy
Requires:       chkconfig
Requires:       chrpath
Requires:       clucene-core
Requires:       cmake
Requires:       compat-db
Requires:       compat-db47
Requires:       compat-gcc-44
Requires:       compat-gcc-44-c++
Requires:       compat-gcc-44-gfortran
Requires:       compat-glibc
Requires:       compat-glibc-headers
Requires:       compat-libcap1
Requires:       compat-libf2c-34
Requires:       compat-libgfortran-41
Requires:       compat-libstdc++-33
Requires:       compat-openldap
Requires:       compat-openldap
Requires:       coreutils
Requires:       cpio
Requires:       cpp
Requires:       cpupowerutils
Requires:       cracklib
Requires:       cracklib-dicts
Requires:       crda
Requires:       createrepo
Requires:       cronie
Requires:       cronie-anacron
Requires:       crontabs
Requires:       cryptsetup-luks
Requires:       cryptsetup-luks-libs
Requires:       cscope
Requires:       ctags
Requires:       ctags-etags
Requires:       cups
Requires:       cups-devel
Requires:       cups-libs
Requires:       curl
Requires:       cvs
Requires:       cvs-inetd
Requires:       cyrus-sasl
Requires:       cyrus-sasl-devel
Requires:       cyrus-sasl-gssapi
Requires:       cyrus-sasl-lib
Requires:       cyrus-sasl-plain
Requires:       db4
Requires:       db4-cxx
Requires:       db4-devel
Requires:       db4-utils
Requires:       dbus
Requires:       dbus-devel
Requires:       dbus-glib
Requires:       dbus-glib-devel
Requires:       dbus-libs
Requires:       dbus-python
Requires:       dbus-x11
Requires:       dcraw
Requires:       dejagnu
Requires:       deltarpm
Requires:       device-mapper
Requires:       device-mapper-event
Requires:       device-mapper-event-libs
Requires:       device-mapper-libs
Requires:       device-mapper-persistent-data
Requires:       dhclient
Requires:       dhcp-common
Requires:       diffstat
Requires:       diffutils
Requires:       dmidecode
Requires:       dmraid
Requires:       dmraid-events
Requires:       docbook-dtds
Requires:       docbook-style-dsssl
Requires:       docbook-style-xsl
Requires:       docbook-utils
Requires:       dos2unix
Requires:       dosfstools
Requires:       doxygen
Requires:       dumpet
Requires:       dvipng
Requires:       e2fsprogs
Requires:       e2fsprogs-devel
Requires:       e2fsprogs-libs
Requires:       ecj
Requires:       ed
Requires:       edac-utils
Requires:       efibootmgr
Requires:       eject
Requires:       ElectricFence
Requires:       elfutils
Requires:       elfutils-devel
Requires:       elfutils-libelf
Requires:       elfutils-libelf-devel
Requires:       elfutils-libs
Requires:       elinks
Requires:       emacs
Requires:       emacs-auctex
Requires:       emacs-common
Requires:       emacs-gnuplot
Requires:       emacs-nox
Requires:       enchant
Requires:       ethtool
Requires:       evince
Requires:       evolution-data-server
Requires:       evolution-data-server-devel
Requires:       evolution-data-server-doc
Requires:       exiv2-libs
Requires:       expat
Requires:       expat-devel
Requires:       expect
Requires:       fakeroot
Requires:       fakeroot-libs
Requires:       fetchmail
Requires:       fftw
Requires:       fftw-devel
Requires:       finger
Requires:       file
Requires:       file-devel
Requires:       file-libs
Requires:       filesystem
Requires:       findutils
Requires:       fipscheck
Requires:       fipscheck-lib
Requires:       flac
Requires:       flex
Requires:       fontconfig
Requires:       fontconfig-devel
Requires:       foomatic
Requires:       foomatic-db
Requires:       foomatic-db-filesystem
Requires:       foomatic-db-ppds
Requires:       fping
Requires:       fprintd
Requires:       fprintd-pam
Requires:       freeglut
Requires:       freeglut-devel
Requires:       freetype
Requires:       freetype-devel
Requires:       ftp
Requires:       fuse
Requires:       fuse-devel
Requires:       fuse-libs
Requires:       gamin
Requires:       gamin-devel
Requires:       ganglia
Requires:       ganglia-gmond
Requires:       gawk
Requires:       gc
Requires:       gcc
Requires:       gcc-c++
Requires:       gcc-gfortran
Requires:       gcc-gnat
Requires:       gcc-objc
Requires:       gcc-objc++
Requires:       GConf2
Requires:       GConf2-devel
Requires:       gd
Requires:       gdb
Requires:       gdbm
Requires:       gegl
Requires:       genisoimage
Requires:       geoclue
Requires:       gettext
Requires:       gettext-devel
Requires:       gettext-libs
Requires:       ghostscript
Requires:       ghostscript-fonts
Requires:       giflib
Requires:       gimp
Requires:       gimp-data-extras
Requires:       gimp-help
Requires:       gimp-libs
Requires:       git
Requires:       git-svn
Requires:       gitk
Requires:       glib2
Requires:       glib2-devel
Requires:       glibc
Requires:       glibc-common
Requires:       glibc-devel
Requires:       glibc-headers
Requires:       glibmm24
Requires:       gmp
Requires:       gmp-devel
Requires:       gnupg2
Requires:       gnuplot
Requires:       gnuplot-common
Requires:       gnutls
Requires:       gnutls-devel
Requires:       gpgme
Requires:       gpm
Requires:       gpm-libs
Requires:       grep
Requires:       groff
Requires:       grub2
Requires:       grubby
Requires:       gsi-openssh
Requires:       gsi-openssh-clients
Requires:       gsl
Requires:       gsl-devel
Requires:       gsm
Requires:       gsoap
Requires:       gstreamer
Requires:       gstreamer-devel
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-base-devel
Requires:       gstreamer-tools
Requires:       gtk2
Requires:       gtk2-devel
Requires:       gtk2-engines
Requires:       gtk-doc
Requires:       gtkmm24
Requires:       gtkspell
Requires:       gutenprint
Requires:       gutenprint-plugin
Requires:       gv
Requires:       gvfs
Requires:       gvfs-devel
Requires:       gzip
Requires:       hdparm
Requires:       HEP_OSlibs
Requires:       hesiod
Requires:       hicolor-icon-theme
Requires:       hmaccalc
Requires:       hplip-common
Requires:       hplip-libs
Requires:       htop
Requires:       httpd
Requires:       httpd-devel
Requires:       httpd-tools
Requires:       hunspell
Requires:       hunspell-devel
Requires:       hunspell-en
Requires:       hwdata
Requires:       ilmbase
Requires:       ImageMagick
Requires:       ImageMagick-c++
Requires:       imake
Requires:       indent
Requires:       info
Requires:       initscripts
Requires:       inkscape
Requires:       intltool
Requires:       ipa-client
Requires:       ipa-python
Requires:       iproute
Requires:       iptables
Requires:       iptables-devel
Requires:       iptables-ipv6
Requires:       iputils
Requires:       irqbalance
Requires:       irssi
Requires:       iscsi-initiator-utils
Requires:       iso-codes
Requires:       ivtv-firmware
Requires:       iw
Requires:       iwl1000-firmware
Requires:       iwl100-firmware
Requires:       iwl3945-firmware
Requires:       iwl4965-firmware
Requires:       iwl5000-firmware
Requires:       iwl5150-firmware
Requires:       iwl6000-firmware
Requires:       iwl6000g2a-firmware
Requires:       iwl6050-firmware
Requires:       jakarta-commons-cli
Requires:       jakarta-commons-discovery
Requires:       jakarta-commons-httpclient
Requires:       jakarta-commons-lang
Requires:       jakarta-commons-logging
Requires:       jasper-libs
Requires:       java-1.6.0-openjdk
Requires:       java-1.6.0-openjdk-devel
Requires:       java-1.7.0-openjdk
Requires:       java-1.7.0-openjdk-devel
Requires:       java-1.8.0-openjdk
Requires:       java-1.8.0-openjdk-devel
Requires:       java_cup
Requires:       jdk
Requires:       jline
Requires:       joe
Requires:       jpackage-utils
Requires:       jss
Requires:       junit
Requires:       jwhois
Requires:       kabi-yum-plugins
Requires:       kbd
Requires:       kbd-misc
Requires:       kdebase-devel
Requires:       kdebase-libs
Requires:       kdebase-runtime
Requires:       kdebase-runtime-libs
Requires:       kdebase-workspace
Requires:       kdebase-workspace-devel
Requires:       kdebase-workspace-libs
Requires:       kdebase-workspace-wallpapers
Requires:       kde-filesystem
Requires:       kdegraphics-devel
Requires:       kdegraphics-libs
Requires:       kdelibs
Requires:       kdelibs3
Requires:       kdelibs-apidocs
Requires:       kdelibs-common
Requires:       kdelibs-devel
Requires:       kdelibs-experimental
Requires:       kdemultimedia-devel
Requires:       kdemultimedia-libs
Requires:       kdenetwork-devel
Requires:       kdepim
Requires:       kdepim-devel
Requires:       kdepimlibs
Requires:       kdepim-libs
Requires:       kdepimlibs-akonadi
Requires:       kdepimlibs-devel
Requires:       kdesdk-devel
Requires:       kde-settings
Requires:       kexec-tools
Requires:       keyutils
Requires:       keyutils-libs
Requires:       keyutils-libs-devel
Requires:       kio_sysinfo
Requires:       kpartx
Requires:       kpathsea
Requires:       krb5-devel
Requires:       krb5-libs
Requires:       krb5-pkinit
Requires:       krb5-workstation
Requires:       ksc
Requires:       ksh
Requires:       ksysguardd
Requires:       ldapjdk
Requires:       ledmon
Requires:       less
Requires:       lftp
Requires:       libacl
Requires:       libacl-devel
Requires:       libaio
Requires:       libaio-devel
Requires:       libao
Requires:       libart_lgpl
Requires:       libart_lgpl-devel
Requires:       libasyncns
Requires:       libatasmart
Requires:       libattr
Requires:       libattr-devel
Requires:       libblkid
Requires:       libblkid-devel
Requires:       libbonobo
Requires:       libbonobo-devel
Requires:       libbonoboui
Requires:       libbonoboui-devel
Requires:       libcanberra
Requires:       libcanberra-devel
Requires:       libcanberra-gtk2
Requires:       libcap
Requires:       libcap-devel
Requires:       libcap-ng
Requires:       libcap-ng-devel
Requires:       libcdio
Requires:       libcollection
Requires:       libcom_err
Requires:       libcom_err-devel
Requires:       libconfuse
Requires:       libcroco
Requires:       libcroco-devel
Requires:       libcurl
Requires:       libcurl-devel
Requires:       libdbi
Requires:       libdbi-dbd-mysql
Requires:       libdbi-drivers
Requires:       libdhash
Requires:       libdmx
Requires:       libdrm
Requires:       libdrm-devel
Requires:       libedit
Requires:       libevent
Requires:       libexif
Requires:       libexif-devel
Requires:       libffi
Requires:       libfontenc
Requires:       libfprint
Requires:       libgcc
Requires:       libgcrypt
Requires:       libgcrypt-devel
Requires:       libgfortran
Requires:       libglade2
Requires:       libglade2-devel
Requires:       libgnat
Requires:       libgnat-devel
Requires:       libgnome
Requires:       libgnomecanvas
Requires:       libgnomecanvas-devel
Requires:       libgnome-devel
Requires:       libgnomeui
Requires:       libgnomeui-devel
Requires:       libgomp
Requires:       libgpg-error
Requires:       libgpg-error-devel
Requires:       libgphoto2
Requires:       libgphoto2-devel
Requires:       libgsf
Requires:       libgsf-devel
Requires:       libgudev1
Requires:       libgudev1-devel
Requires:       libgweather
Requires:       libgweather-devel
Requires:       libhugetlbfs
Requires:       libhugetlbfs-devel
Requires:       libibcm
Requires:       libibverbs-devel
Requires:       libical
Requires:       libical-devel
Requires:       libICE
Requires:       libICE-devel
Requires:       libicu
Requires:       libIDL
Requires:       libIDL-devel
Requires:       libidn
Requires:       libidn-devel
Requires:       libieee1284
Requires:       libieee1284-devel
Requires:       libini_config
Requires:       libipa_hbac
Requires:       libipa_hbac-python
Requires:       libjpeg-turbo
Requires:       libjpeg-turbo-devel
Requires:       libldb
Requires:       libmng
Requires:       libnl
Requires:       libnl-devel
Requires:       libnotify
Requires:       libnotify-devel
Requires:       libobjc
Requires:       libogg
Requires:       liboil
Requires:       libopenraw
Requires:       libotf
Requires:       libpath_utils
Requires:       libpcap
Requires:       libpciaccess
Requires:       libpng
Requires:       libpng-devel
Requires:       libproxy
Requires:       libproxy-bin
Requires:       libproxy-python
Requires:       librdmacm
Requires:       libref_array
Requires:       librelp
Requires:       libreport
Requires:       libreport-cli
Requires:       libreport-compat
Requires:       libreport-plugin-kerneloops
Requires:       libreport-plugin-logger
Requires:       libreport-plugin-mailx
Requires:       libreport-plugin-reportuploader
Requires:       libreport-plugin-ureport
Requires:       libreport-python
Requires:       librsvg2
Requires:       librsvg2-devel
Requires:       libsamplerate
Requires:       libsane-hpaio
Requires:       libselinux
Requires:       libselinux-devel
Requires:       libselinux-python
Requires:       libselinux-utils
Requires:       libsemanage
Requires:       libsepol
Requires:       libsepol-devel
Requires:       libsigc++20
Requires:       libSM
Requires:       libsmbclient
Requires:       libSM-devel
Requires:       libsndfile
Requires:       libsoup
Requires:       libsoup-devel
Requires:       libspiro
Requires:       libss
Requires:       libssh2
Requires:       libsss_autofs
Requires:       libsss_idmap
Requires:       libsss_sudo
Requires:       libstdc++
Requires:       libstdc++-devel
Requires:       libstdc++-docs
Requires:       libsysfs
Requires:       libtalloc
Requires:       libtar
Requires:       libtasn1
Requires:       libtasn1-devel
Requires:       libtdb
Requires:       libtevent
Requires:       libthai
Requires:       libtheora
Requires:       libtidy
Requires:       libtiff
Requires:       libtiff-devel
Requires:       libtirpc
Requires:       libtool
Requires:       libtool-ltdl
Requires:       libusb
Requires:       libusb1
Requires:       libusb-devel
Requires:       libuser
Requires:       libutempter
Requires:       libuuid
Requires:       libuuid-devel
Requires:       libv4l
Requires:       libvisual
Requires:       libvorbis
Requires:       libwmf
Requires:       libwmf-lite
Requires:       libwnck
Requires:       libwpd
Requires:       libwpg
Requires:       libX11
Requires:       libX11-common
Requires:       libX11-devel
Requires:       libXau
Requires:       libXau-devel
Requires:       libXaw
Requires:       libXaw-devel
Requires:       libxcb
Requires:       libxcb-devel
Requires:       libXcomposite
Requires:       libXcomposite-devel
Requires:       libXcursor
Requires:       libXcursor-devel
Requires:       libXdamage
Requires:       libXdamage-devel
Requires:       libXdmcp
Requires:       libXdmcp-devel
Requires:       libXext
Requires:       libXext-devel
Requires:       libXfixes
Requires:       libXfixes-devel
Requires:       libXfont
Requires:       libXft
Requires:       libXft-devel
Requires:       libXi
Requires:       libXi-devel
Requires:       libXinerama
Requires:       libXinerama-devel
Requires:       libxkbfile
Requires:       libxkbfile-devel
Requires:       libxklavier
Requires:       libxml2
Requires:       libxml2-devel
Requires:       libxml2-python
Requires:       libXmu
Requires:       libXmu-devel
Requires:       libXp
Requires:       libXp-devel
Requires:       libXpm
Requires:       libXpm-devel
Requires:       libXrandr
Requires:       libXrandr-devel
Requires:       libXrender
Requires:       libXrender-devel
Requires:       libXres
Requires:       libXScrnSaver
Requires:       libXScrnSaver-devel
Requires:       libxslt
Requires:       libxslt-devel
Requires:       libXt
Requires:       libXt-devel
Requires:       libXtst
Requires:       libXtst-devel
Requires:       libXv
Requires:       libXv-devel
Requires:       libXxf86dga
Requires:       libXxf86misc
Requires:       libXxf86misc-devel
Requires:       libXxf86vm
Requires:       libXxf86vm-devel
Requires:       linuxptp
Requires:       lm_sensors
Requires:       lm_sensors-devel
Requires:       lm_sensors-libs
Requires:       lockdev
Requires:       log4cplus
Requires:       log4cplus-devel
Requires:       log4cpp-devel
Requires:       log4j
Requires:       logrotate
Requires:       logwatch
Requires:       lrzsz
Requires:       lsof
Requires:       lua
Requires:       lvm2
Requires:       lvm2-libs
Requires:       m17n-db
Requires:       m17n-db-datafiles
Requires:       m17n-lib
Requires:       m4
Requires:       mailcap
Requires:       mailx
Requires:       make
Requires:       man
Requires:       man-pages
Requires:       man-pages-overrides
Requires:       mariadb-devel
Requires:       mariadb-libs
Requires:       mariadb-server
Requires:       mc
Requires:       mdadm
Requires:       mercurial
Requires:       mesa-dri-drivers
Requires:       mesa-dri-filesystem
Requires:       mesa-libGL
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU
Requires:       mesa-libGLU-devel
Requires:       microcode_ctl
Requires:       mkbootdisk
Requires:       mlocate
Requires:       mod_dav_svn
Requires:       mod_perl
Requires:       module-init-tools
Requires:       mpfr
Requires:       mpich
Requires:       mpich-devel
Requires:       mtools
Requires:       mtr
Requires:       mutt
Requires:       mysql-connector-java
Requires:       mysql-connector-odbc
Requires:       MySQL-python
Requires:       nano
Requires:       nasm
Requires:       ncurses
Requires:       ncurses-base
Requires:       ncurses-devel
Requires:       ncurses-libs
Requires:       ncurses-term
Requires:       neon
Requires:       netpbm
Requires:       netpbm-progs
Requires:       net-snmp-devel
Requires:       net-snmp-libs
Requires:       net-snmp-utils
Requires:       net-tools
Requires:       NetworkManager-glib
Requires:       newt
Requires:       newt-python
Requires:       nfs-utils
Requires:       notification-daemon
Requires:       nscd
Requires:       nspr
Requires:       nspr-devel
Requires:       nss
Requires:       nss_compat_ossl
Requires:       nss-devel
Requires:       nss-pam-ldapd
Requires:       nss-softokn
Requires:       nss-softokn-devel
Requires:       nss-softokn-freebl
Requires:       nss-softokn-freebl-devel
Requires:       nss-sysinit
Requires:       nss-tools
Requires:       nss-util
Requires:       nss-util-devel
Requires:       ntp
Requires:       ntpdate
Requires:       ntsysv
Requires:       numactl
Requires:       numactl-devel
Requires:       numpy
Requires:       oddjob
Requires:       oddjob-mkhomedir
Requires:       OpenEXR-libs
Requires:       openjade
Requires:       openjpeg-libs
Requires:       openldap
Requires:       openldap-clients
Requires:       openldap-devel
Requires:       openmotif
Requires:       openmotif-devel
Requires:       opensp
Requires:       openssh
Requires:       openssh-clients
Requires:       openssh-server
Requires:       openssl
Requires:       openssl098e
Requires:       openssl-devel
Requires:       ORBit2
Requires:       ORBit2-devel
Requires:       oxygen-cursor-themes
Requires:       oxygen-icon-theme
Requires:       pakchois
Requires:       pam
Requires:       pam_krb5
Requires:       pango
Requires:       pango-devel
Requires:       pangomm
Requires:       papi
Requires:       papi-devel
Requires:       parted
Requires:       passwd
Requires:       patch
Requires:       patchutils
Requires:       pax
Requires:       pciutils
Requires:       pciutils-libs
Requires:       pcre
Requires:       pcre-devel
Requires:       perl
Requires:       perl-Archive-Extract
Requires:       perl-Archive-Tar
Requires:       perl-Authen-SASL
Requires:       perl-Bit-Vector
Requires:       perl-BSD-Resource
Requires:       perl-Carp-Clan
Requires:       perl-CGI
Requires:       perl-common-sense
Requires:       perl-Compress-Raw-Bzip2
Requires:       perl-Compress-Raw-Zlib
Requires:       perl-Compress-Zlib
Requires:       perl-Convert-ASN1
Requires:       perl-core
Requires:       perl-CPAN
Requires:       perl-CPANPLUS
Requires:       perl-Crypt-SSLeay
Requires:       perl-Date-Calc
Requires:       perl-Date-Manip
Requires:       perl-DBD-MySQL
Requires:       perl-DBD-SQLite
Requires:       perl-DBI
Requires:       perl-DBIx-Simple
Requires:       perl-devel
Requires:       perl-Devel-Symdump
Requires:       perl-Digest-HMAC
Requires:       perl-Digest-SHA
Requires:       perl-Digest-SHA1
Requires:       perl-Error
Requires:       perl-ExtUtils-CBuilder
Requires:       perl-ExtUtils-Embed
Requires:       perl-ExtUtils-MakeMaker
Requires:       perl-ExtUtils-ParseXS
Requires:       perl-File-Fetch
Requires:       perl-Frontier-RPC
Requires:       perl-Frontier-RPC-Client
Requires:       perl-Frontier-RPC-doc
Requires:       perl-Git
Requires:       perl-GSSAPI
Requires:       perl-HTML-Parser
Requires:       perl-HTML-Tagset
Requires:       perl-IO-Compress-Base
Requires:       perl-IO-Compress-Bzip2
Requires:       perl-IO-Compress-Zlib
Requires:       perl-IO-Socket-SSL
Requires:       perl-IO-String
Requires:       perl-IO-Zlib
Requires:       perl-IPC-Cmd
Requires:       perl-JSON-XS
Requires:       perl-LDAP
Requires:       perl-libs
Requires:       perl-libwww-perl
Requires:       perl-libxml-perl
Requires:       perl-Locale-Maketext-Simple
Requires:       perl-Log-Message
Requires:       perl-Log-Message-Simple
Requires:       perl-Module-Build
Requires:       perl-Module-CoreList
Requires:       perl-Module-Load
Requires:       perl-Module-Load-Conditional
Requires:       perl-Module-Loaded
Requires:       perl-Module-Pluggable
Requires:       perl-Mozilla-LDAP
Requires:       perl-Net-LibIDN
Requires:       perl-Net-SSLeay
Requires:       perl-Object-Accessor
Requires:       perl-Package-Constants
Requires:       perl-Params-Check
Requires:       perl-parent
Requires:       perl-Parse-CPAN-Meta
Requires:       perl-Pod-Coverage
Requires:       perl-Pod-Escapes
Requires:       perl-Pod-POM
Requires:       perl-Pod-Simple
Requires:       perl-Proc-ProcessTable
Requires:       perl-Readonly
Requires:       perl-Readonly-XS
Requires:       perl-SGMLSpm
Requires:       perl-Template-Toolkit
Requires:       perl-TermReadKey
Requires:       perl-Term-UI
Requires:       perl-Test-Harness
Requires:       perl-Test-Pod
Requires:       perl-Test-Pod-Coverage
Requires:       perl-Test-Simple
Requires:       perl-TeX-Hyphen
Requires:       perl-Text-Autoformat
Requires:       perl-Text-Iconv
Requires:       perl-Text-Reform
Requires:       perltidy
Requires:       perl-Time-HiRes
Requires:       perl-Time-Piece
Requires:       perl-URI
Requires:       perl-version
Requires:       perl-XML-DOM
Requires:       perl-XML-Dumper
Requires:       perl-XML-Filter-BufferText
Requires:       perl-XML-Grove
Requires:       perl-XML-LibXML
Requires:       perl-XML-NamespaceSupport
Requires:       perl-XML-Parser
Requires:       perl-XML-RegExp
Requires:       perl-XML-SAX
Requires:       perl-XML-SAX-Writer
Requires:       perl-XML-Simple
Requires:       perl-XML-Twig
Requires:       perl-YAML-Syck
Requires:       phonon-backend-gstreamer
Requires:       php
Requires:       pinentry
Requires:       pinfo
Requires:       pixman
Requires:       pixman-devel
Requires:       pkgconfig
Requires:       plymouth
Requires:       plymouth-core-libs
Requires:       plymouth-scripts
Requires:       pm-utils
Requires:       policycoreutils
Requires:       polkit
Requires:       polkit-devel
Requires:       polkit-docs
Requires:       polkit-gnome
Requires:       poppler
Requires:       poppler-data
Requires:       poppler-glib
Requires:       poppler-utils
Requires:       popt
Requires:       popt-devel
Requires:       portreserve
Requires:       postfix
Requires:       postgresql
Requires:       postgresql-devel
Requires:       postgresql-libs
Requires:       prelink
Requires:       procmail
Requires:       procps
Requires:       psacct
Requires:       psmisc
Requires:       psutils
Requires:       pth
Requires:       pulseaudio-libs
Requires:       pulseaudio-libs-devel
Requires:       pulseaudio-libs-glib2
Requires:       pulseaudio-module-zeroconf
Requires:       pycairo
Requires:       pycairo-devel
Requires:       pygobject2
Requires:       pygobject2-codegen
Requires:       pygobject2-devel
Requires:       pygobject2-doc
Requires:       pygpgme
Requires:       pygtk2
Requires:       pygtk2-codegen
Requires:       pygtk2-devel
Requires:       pygtk2-doc
Requires:       pyOpenSSL
Requires:       PyPAM
Requires:       PyQt4
Requires:       PyQt4-devel
Requires:       pytalloc
Requires:       python
Requires:       python-babel
Requires:       python-crypto
Requires:       python-dateutil
Requires:       python-deltarpm
Requires:       python-devel
Requires:       python-dmidecode
Requires:       python-docs
Requires:       python-enchant
Requires:       python-ethtool
Requires:       python-iniparse
Requires:       python-kerberos
Requires:       python-krbV
Requires:       python-ldap
Requires:       python-libs
Requires:       python-lxml
Requires:       python-magic
Requires:       python-netaddr
Requires:       python-nose
Requires:       python-nss
Requires:       python-paramiko
Requires:       python-pip
Requires:       python-pycurl
Requires:       python-setuptools
Requires:       python-urlgrabber
Requires:       python-volume_key
Requires:       python34
Requires:       python34-libs
Requires:       python34-scipy
Requires:       python34-numpy
Requires:       qca2
Requires:       qimageblitz
Requires:       qstat
Requires:       qt
Requires:       qt3
Requires:       qt-devel
Requires:       qt-mysql
Requires:       qt-sqlite
Requires:       qt-x11
Requires:       quota
Requires:       raptor2
Requires:       rarian
Requires:       rarian-compat
Requires:       rasqal
Requires:       rcs
Requires:       rdate
Requires:       readline
Requires:       readline-devel
Requires:       redhat-logos
Requires:       redhat-lsb
Requires:       redhat-lsb-compat
Requires:       redhat-lsb-core
Requires:       redhat-lsb-printing
Requires:       redhat-menus
Requires:       redhat-rpm-config
Requires:       redland
Requires:       regexp
Requires:       rfkill
Requires:       rh-python36-python-docutils-0.14-1.el7.noarch
Requires:       rh-python36-python-sphinx-1.2.3-3.el7.noarch
Requires:       rh-python36-python-coverage-4.4.1-2.el7.x86_64
Requires:       rh-python36-python-virtualenv-15.1.0-2.el7.noarch
Requires:       rh-python36-python-PyMySQL-0.7.11-1.el7.noarch
Requires:       rh-python36-python-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-markupsafe-1.0-1.el7.x86_64
Requires:       rh-python36-python-debug-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-pip-9.0.1-2.el7.noarch
Requires:       rh-python36-python-bson-3.5.1-1.el7.x86_64
Requires:       rh-python36-python-psycopg2-doc-2.7.3-1.el7.x86_64
Requires:       rh-python36-scldevel-2.0-1.el7.x86_64
Requires:       rh-python36-python-devel-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-six-1.11.0-1.el7.noarch
Requires:       rh-python36-runtime-2.0-1.el7.x86_64
Requires:       rh-python36-python-tkinter-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-pygments-2.2.0-1.el7.noarch
Requires:       rh-python36-python-sphinx-doc-1.2.3-3.el7.noarch
Requires:       rh-python36-build-2.0-1.el7.x86_64
Requires:       rh-python36-PyYAML-3.12-1.el7.x86_64
Requires:       rh-python36-python-tools-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-babel-2.5.1-1.el7.noarch
Requires:       rh-python36-mod_wsgi-4.5.18-1.el7.x86_64
Requires:       rh-python36-python-nose-docs-1.3.7-3.el7.noarch
Requires:       rh-python36-python-pymongo-doc-3.5.1-1.el7.x86_64
Requires:       rh-python36-python-nose-1.3.7-3.el7.noarch
Requires:       rh-python36-python-test-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-jinja2-2.9.6-2.el7.noarch
Requires:       rh-python36-scipy-0.19.1-2.el7.x86_64
Requires:       rh-python36-python-simplejson-3.11.1-1.el7.x86_64
Requires:       rh-python36-numpy-1.13.1-1.el7.x86_64
Requires:       rh-python36-2.0-1.el7.x86_64
Requires:       rh-python36-python-libs-3.6.3-3.el7.x86_64
Requires:       rh-python36-python-psycopg2-2.7.3-1.el7.x86_64
Requires:       rh-python36-babel-2.5.1-1.el7.noarch
Requires:       rh-python36-numpy-f2py-1.13.1-1.el7.x86_64
Requires:       rh-python36-python-sqlalchemy-1.1.14-1.el7.x86_64
Requires:       rh-python36-python-wheel-0.30.0a0-1.el7.noarch
Requires:       rh-python36-python-setuptools-36.5.0-1.el7.noarch
Requires:       rh-python36-python-pymongo-3.5.1-1.el7.x86_64
Requires:       rh-python36-python-pymongo-gridfs-3.5.1-1.el7.x86_64
Requires:       rhino
Requires:       rng-tools
Requires:       rootfiles
Requires:       rpcbind
Requires:       rpm
Requires:       rpm-build
Requires:       rpm-devel
Requires:       rpmdevtools
Requires:       rpm-libs
Requires:       rpmlint
Requires:       rpm-python
Requires:       rsync
Requires:       rsyslog
Requires:       rsyslog-gnutls
Requires:       rsyslog-gssapi
Requires:       rsyslog-relp
Requires:       samba4-libs
Requires:       samba-client
Requires:       samba-common
Requires:       samba-winbind
Requires:       samba-winbind-clients
Requires:       sane-backends
Requires:       sane-backends-devel
Requires:       sane-backends-libs
Requires:       sane-frontends
Requires:       scl-utils
Requires:       screen
Requires:       SDL
Requires:       SDL-devel
Requires:       sed
Requires:       selinux-policy
Requires:       selinux-policy-targeted
Requires:       setserial
Requires:       setup
Requires:       setuptool
Requires:       sg3_utils-libs
Requires:       sgml-common
Requires:       sgpio
Requires:       shadow-utils
Requires:       shared-mime-info
Requires:       sip
Requires:       sip-devel
Requires:       slang
Requires:       slf4j
Requires:       smartmontools
Requires:       smp_utils
Requires:       soprano
Requires:       sos
Requires:       sox
Requires:       sqlite
Requires:       sqlite-devel
Requires:       squashfs-tools
Requires:       srm-ifce
Requires:       sssd
Requires:       sssd-client
Requires:       star
Requires:       startup-notification
Requires:       startup-notification-devel
Requires:       strace
Requires:       strigi-devel
Requires:       strigi-libs
Requires:       subversion
Requires:       sudo
Requires:       svrcore
Requires:       svrcore-devel
Requires:       swig
Requires:       sysfsutils
Requires:       syslinux
Requires:       sysstat
Requires:       system-config-firewall-base
Requires:       system-config-firewall-tui
Requires:       systemtap
Requires:       systemtap-client
Requires:       systemtap-devel
Requires:       systemtap-runtime
Requires:       systemtap-sdt-devel
Requires:       systemtap-server
Requires:       sysvinit-tools
Requires:       tkinter
Requires:       t1lib
Requires:       tar
Requires:       tbb
Requires:       tbb-devel
Requires:       tboot
Requires:       tcl
Requires:       tcl-devel
Requires:       tcpdump
Requires:       tcp_wrappers
Requires:       tcp_wrappers-devel
Requires:       tcp_wrappers-libs
Requires:       tcsh
Requires:       texlive
Requires:       texlive-dvips
Requires:       texlive-latex
Requires:       tex-preview
Requires:       tidy
Requires:       time
Requires:       tk
Requires:       tk-devel
Requires:       tmpwatch
Requires:       tokyocabinet
Requires:       traceroute
Requires:       transfig
Requires:       trousers
Requires:       ttmkfdir
Requires:       tzdata
Requires:       tzdata-java
Requires:       uberftp
Requires:       udev
Requires:       udftools
Requires:       unique
Requires:       unique-devel
Requires:       unix2dos
Requires:       unixODBC
Requires:       unixODBC-devel
Requires:       unzip
Requires:       urlview
Requires:       urw-fonts
Requires:       usbutils
Requires:       usermode
Requires:       ustr
Requires:       util-linux-ng
Requires:       uuidd
Requires:       valgrind
Requires:       vconfig
Requires:       vim-common
Requires:       vim-enhanced
Requires:       vim-minimal
Requires:       virt-what
Requires:       volume_key
Requires:       volume_key-libs
Requires:       wavpack
Requires:       wget
Requires:       which
Requires:       wireless-tools
Requires:       wodim
Requires:       words
Requires:       wsdl4j
Requires:       x86info
Requires:       Xaw3d
Requires:       xcb-util
Requires:       xclip
Requires:       xdg-user-dirs
Requires:       xdg-utils
Requires:       xdvik
Requires:       xdvipdfmx
Requires:       xemacs
Requires:       xerces-c
Requires:       xerces-j2
Requires:       xfig
Requires:       xfig-common
Requires:       xfig-plain
Requires:       xinetd
Requires:       xml-common
Requires:       xml-commons-apis
Requires:       xml-commons-resolver
Requires:       xmlrpc-c
Requires:       xmlrpc-c-client
Requires:       xorg-x11-apps
Requires:       xorg-x11-xbitmaps
Requires:       xorg-x11-drv-ati-firmware
Requires:       xorg-x11-fonts-misc
Requires:       xorg-x11-fonts-Type1
Requires:       xorg-x11-font-utils
Requires:       xorg-x11-proto-devel
Requires:       xorg-x11-server-utils
Requires:       xorg-x11-utils
Requires:       xorg-x11-xauth
Requires:       xorg-x11-xinit
Requires:       xrootd-devel
Requires:       xpdf
Requires:       xsane
Requires:       xsane-common
Requires:       xsane-gimp
Requires:       xz
Requires:       xz-devel
Requires:       xz-libs
Requires:       xz-lzma-compat
Requires:       ypbind
Requires:       yp-tools
Requires:       yum
Requires:       yum-cron
Requires:       yum-metadata-parser
Requires:       yum-plugin-aliases
Requires:       yum-plugin-changelog
Requires:       yum-plugin-downloadonly
Requires:       yum-plugin-security
Requires:       yum-plugin-tmprepo
Requires:       yum-plugin-verify
Requires:       yum-plugin-versionlock
Requires:       yum-presto
Requires:       yum-utils
Requires:       zip
Requires:       zlib
Requires:       zlib-devel
Requires:       zsh
#Source:		wn65pkg-1.0.1.tar.gz

%description
Meta Packages for speed up puppet configuration
yanxf@ihep.ac.cn
%prep

%build
# Nothing to do

%install
rm -rf $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT
 find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
 find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%changelog
* Thu Nov 30 2017 Yan Xiaofei <yanxf@ihep.ac.cn> - 1.0.0-1
- First version for wn74pkg
