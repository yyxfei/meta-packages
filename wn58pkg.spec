Name:		wn58pkg
Version:	1.0.1
Release:	3%{?dist}
Summary:	WN58 meta-packages
Group:		Applications/Internet
License:	ASL 2.0
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       915resolution
Requires:       a2ps
Requires:       acl
Requires:       acpid
Requires:       adjtimex
Requires:       afstokenspatch
Requires:       agg
Requires:       aide
Requires:       alpine
Requires:       alsa-lib-devel
Requires:       alsa-lib
Requires:       alsa-utils
Requires:       amanda-client
Requires:       amanda-server
Requires:       amanda
Requires:       amtu
Requires:       am-utils
Requires:       anacron
Requires:       antlr
Requires:       apr-util
Requires:       apr
Requires:       arptables_jf
Requires:       arpwatch
Requires:       arts
Requires:       aspell-en
Requires:       aspell
Requires:       atk-devel
Requires:       atk
Requires:       atlas
Requires:       at-spi
Requires:       attr
Requires:       at
Requires:       audiofile-devel
Requires:       audiofile
Requires:       audit-libs
Requires:       audit-libs-python
Requires:       audit
Requires:       aufs
Requires:       augeas
Requires:       authconfig-gtk
Requires:       authconfig
Requires:       authd
Requires:       autoconf
Requires:       automake14
Requires:       automake15
Requires:       automake16
Requires:       automake17
Requires:       automake
Requires:       avahi-compat-libdns_sd
Requires:       avahi-glib
Requires:       avahi-qt3
Requires:       avahi-tools
Requires:       avahi
Requires:       basesystem
Requires:       bash
Requires:       bc
Requires:       bind-libs
Requires:       bind-utils
Requires:       binutils220
Requires:       binutils
Requires:       bison
Requires:       bitmap-fonts
Requires:       bitstream-vera-fonts
Requires:       blas-devel
Requires:       blas
Requires:       blktrace
Requires:       bluez-gnome
Requires:       bluez-hcidump
Requires:       bluez-libs
Requires:       bluez-utils-cups
Requires:       bluez-utils
Requires:       boost141-python
Requires:       boost-devel
Requires:       boost
Requires:       boost141-filesystem
Requires:       bouncycastle
Requires:       bridge-utils
Requires:       brlapi
Requires:       brltty
Requires:       busybox
Requires:       byacc
Requires:       bzip2-devel
Requires:       bzip2-libs
Requires:       bzip2
Requires:       cadaver
Requires:       cairo-devel
Requires:       cairo
Requires:       c-ares
Requires:       CASTOR-client
Requires:       c-check
Requires:       ccid
Requires:       cdparanoia-libs
Requires:       cernlib
Requires:       cfitsio
Requires:       CGSI-gSOAP
Requires:       checkpolicy
Requires:       chkconfig
Requires:       chkfontpath
Requires:       classads
Requires:       cmake
Requires:       compat-dapl-devel
Requires:       compat-dapl-static
Requires:       compat-dapl-utils
Requires:       compat-dapl
Requires:       compat-db
Requires:       compat-gcc-34-c++
Requires:       compat-gcc-34-g77
Requires:       compat-gcc-34
Requires:       compat-glibc-headers
Requires:       compat-glibc
Requires:       compat-libf2c-34
Requires:       compat-libgcc-296
Requires:       compat-libstdc++-296
Requires:       compat-libstdc++-33
Requires:       compat-openldap
Requires:       compat-readline43
Requires:       comps-extras
Requires:       conman
Requires:       convmv
Requires:       coolkey-devel
Requires:       coolkey
Requires:       coreutils
Requires:       cpio
Requires:       cpp
Requires:       cpufreq-utils
Requires:       cpuspeed
Requires:       cracklib-dicts
Requires:       cracklib
Requires:       crash
Requires:       createrepo
Requires:       crontabs
Requires:       cryptsetup-luks
Requires:       cscope
Requires:       ctags
Requires:       cups-libs
Requires:       cups
Requires:       curl-devel
Requires:       curl
Requires:       cvs
Requires:       cyrus-sasl-devel
Requires:       cyrus-sasl-gssapi
Requires:       cyrus-sasl-lib
Requires:       cyrus-sasl-plain
Requires:       cyrus-sasl
Requires:       dapl-devel
Requires:       dapl-static
Requires:       dapl-utils
Requires:       dapl
Requires:       db4-devel
Requires:       db4
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       dbus-glib
Requires:       dbus-libs
Requires:       dbus-python
Requires:       dbus
Requires:       dcraw
Requires:       dejagnu
Requires:       dejavu-lgc-fonts
Requires:       Deployment_Guide-en-US
Requires:       dev86
Requires:       device-mapper-event
Requires:       device-mapper
Requires:       device-mapper-multipath
Requires:       dhclient
Requires:       dhcpv6-client
Requires:       dhcpv6
Requires:       dhcp
Requires:       dialog
Requires:       diffstat
Requires:       diffutils
Requires:       dkms
Requires:       dmidecode
Requires:       dmraid-events-logwatch
Requires:       dmraid-events
Requires:       dmraid
Requires:       dnsmasq
Requires:       docbook-dtds
Requires:       dogtail
Requires:       dos2unix
Requires:       dosfstools
Requires:       doxygen
Requires:       dropit
Requires:       dstat
Requires:       dtach
Requires:       dump
Requires:       e2fsprogs-devel
Requires:       e2fsprogs-libs
Requires:       e2fsprogs
Requires:       e4fsprogs
Requires:       ecryptfs-utils
Requires:       edac-utils
Requires:       editline
Requires:       ed
Requires:       efax
Requires:       eject
Requires:       ElectricFence
Requires:       elfutils-libelf-devel-static
Requires:       elfutils-libelf-devel
Requires:       elfutils-libelf
Requires:       elfutils-libs
Requires:       elfutils
Requires:       elinks
Requires:       emacs-common
Requires:       emacs-leim
Requires:       emacs-nox
Requires:       emacspeak
Requires:       emacs
Requires:       enscript
Requires:       epic
Requires:       esound-devel
Requires:       esound
Requires:       ethtool
Requires:       evince
Requires:       evolution-data-server
Requires:       expat-devel
Requires:       expat
Requires:       expect
Requires:       fbset
Requires:       fcoe-utils
Requires:       festival
Requires:       fetchmail
Requires:       fftw3-devel
Requires:       fftw3
Requires:       filesystem
Requires:       file
Requires:       findutils
Requires:       finger
Requires:       fipscheck-devel
Requires:       fipscheck-lib
Requires:       fipscheck
Requires:       firstboot-tui
Requires:       firstboot
Requires:       flex
Requires:       fontconfig-devel
Requires:       fontconfig
Requires:       foomatic
Requires:       fping
Requires:       freeglut
Requires:       freeipmi
Requires:       freeradius
Requires:       freetype-devel
Requires:       freetype
Requires:       fribidi
Requires:       ftp
Requires:       fuse-devel
Requires:       fuse-libs
Requires:       fuse
Requires:       gail
Requires:       gamin
Requires:       gawk
Requires:       gcc44-c++
Requires:       gcc44-gfortran
Requires:       gcc44
Requires:       gcc-c++
Requires:       gcc-gfortran
Requires:       gcc-gnat
Requires:       gcc-objc
Requires:       gcc
Requires:       GConf2-devel
Requires:       GConf2
Requires:       gdbm-devel
Requires:       gdbm
Requires:       gdb
Requires:       gd-devel
Requires:       gdm
Requires:       gd
Requires:       gettext
Requires:       ghostscript-fonts
Requires:       ghostscript
Requires:       giflib-devel
Requires:       giflib
Requires:       gimp-data-extras
Requires:       gimp-help
Requires:       gimp-libs
Requires:       gimp-print-plugin
Requires:       gimp-print
Requires:       gimp
Requires:       gjdoc
Requires:       glib2-devel
Requires:       glib2
Requires:       glibc-common
Requires:       glibc-devel
Requires:       glibc-headers
Requires:       glibc
Requires:       glibmm24
Requires:       glx-utils
Requires:       gmp-devel
Requires:       gmp
Requires:       gnu-crypto-sasl-jdk1.4
Requires:       gnupg2
Requires:       gnupg
Requires:       gnuplot-emacs
Requires:       gnuplot
Requires:       gnutls
Requires:       gnutls-utils
Requires:       gphoto2
Requires:       gpm-devel
Requires:       gpm
Requires:       grep
Requires:       groff
Requires:       grub
Requires:       gsi-openssh-clients
Requires:       gsi-openssh
Requires:       gsl-devel
Requires:       gsl
Requires:       gsoap
Requires:       gtk2-devel
Requires:       gtk2-engines
Requires:       gtk2
Requires:       gtkhtml2
Requires:       gv
Requires:       gzip
Requires:       hal-cups-utils
Requires:       hal-devel
Requires:       hal
Requires:       hardlink
Requires:       hdparm
Requires:       HEP_OSlibs_SL5
Requires:       hesinfo
Requires:       hesiod-devel
Requires:       hesiod
Requires:       hfsutils
Requires:       hicolor-icon-theme
Requires:       hmaccalc
Requires:       hpijs3
Requires:       hpijs
Requires:       hplip3-common
Requires:       hplip3-libs
Requires:       hplip3
Requires:       hplip
Requires:       htdig
Requires:       htmlview
Requires:       httpd
Requires:       hwbrowser
Requires:       hwdata
Requires:       ibsim
Requires:       ibutils-libs
Requires:       ibutils
Requires:       ibvexdmtools
Requires:       icon-naming-utils
Requires:       icon-slicer
Requires:       ifd-egate
Requires:       ImageMagick
Requires:       imake
Requires:       indent
Requires:       infiniband-diags
Requires:       info
Requires:       initscripts
Requires:       iproute
Requires:       ipsec-tools
Requires:       iptables-ipv6
Requires:       iptables
Requires:       iptraf
Requires:       iptstate
Requires:       iputils
Requires:       ipw2100-firmware
Requires:       ipw2200-firmware
Requires:       irda-utils
Requires:       irqbalance
Requires:       iscsi-initiator-utils
Requires:       isdn4k-utils
Requires:       is-interface
Requires:       jakarta-commons-cli
Requires:       jakarta-commons-lang
Requires:       jakarta-commons-logging
Requires:       java-1.4.2-gcj-compat
Requires:       java-1.6.0-openjdk-devel
Requires:       java-1.6.0-openjdk
Requires:       jclassads
Requires:       jdk
Requires:       joe
Requires:       jpackage-utils
Requires:       jwhois
Requires:       kbd
Requires:       kdebase
Requires:       kdeedu
Requires:       kdegraphics
Requires:       kdelibs
Requires:       kdnssd-avahi
Requires:       kexec-tools
Requires:       keyutils-libs-devel
Requires:       keyutils-libs
Requires:       keyutils
Requires:       kpartx
Requires:       krb5-auth-dialog
Requires:       krb5-devel
Requires:       krb5-libs
Requires:       krb5-server
Requires:       krb5-workstation
Requires:       ksh
Requires:       ktune
Requires:       kudzu-devel
Requires:       kudzu
Requires:       lam-libs
Requires:       lam
Requires:       lapack-devel
Requires:       lapack
Requires:       less
Requires:       lftp
Requires:       libacl-devel
Requires:       libacl
Requires:       libaio
Requires:       libart_lgpl-devel
Requires:       libart_lgpl
Requires:       libassuan-devel
Requires:       libattr-devel
Requires:       libattr
Requires:       libbonobo-devel
Requires:       libbonoboui-devel
Requires:       libbonoboui
Requires:       libbonobo
Requires:       libcap-devel
Requires:       libcap
Requires:       libcollection
Requires:       libcroco
Requires:       libcxgb3
Requires:       libcxgb4
Requires:       libdaemon
Requires:       libdbi-dbd-mysql
Requires:       libdbi-drivers
Requires:       libdbi
Requires:       libdhash
Requires:       libdmx
Requires:       libdrm-devel
Requires:       libdrm
Requires:       liberation-fonts
Requires:       libevent
Requires:       libexif
Requires:       libffi
Requires:       libfontenc-devel
Requires:       libfontenc
Requires:       libFS
Requires:       libgcc
Requires:       libgcj-devel
Requires:       libgcj
Requires:       libgcrypt-devel
Requires:       libgcrypt
Requires:       libgfortran44
Requires:       libgfortran
Requires:       libglade2-devel
Requires:       libglade2
Requires:       libgnat
Requires:       libgnomecanvas-devel
Requires:       libgnomecanvas
Requires:       libgnomecups
Requires:       libgnome-devel
Requires:       libgnomeprint22
Requires:       libgnomeprintui22
Requires:       libgnomeui-devel
Requires:       libgnomeui
Requires:       libgnome
Requires:       libgomp
Requires:       libgpg-error-devel
Requires:       libgpg-error
Requires:       libgsf
Requires:       libgssapi
Requires:       libhbaapi-devel
Requires:       libhbaapi
Requires:       libhbalinux
Requires:       libhugetlbfs
Requires:       libibcm
Requires:       libibcommon-devel
Requires:       libibcommon
Requires:       libibmad
Requires:       libibumad-devel
Requires:       libibumad
Requires:       libibverbs-devel
Requires:       libibverbs-utils
Requires:       libibverbs
Requires:       libICE-devel
Requires:       libICE
Requires:       libicu
Requires:       libIDL-devel
Requires:       libIDL
Requires:       libidn-devel
Requires:       libidn
Requires:       libieee1284
Requires:       libini_config
Requires:       libipa_hbac
Requires:       libipathverbs
Requires:       libjpeg-devel
Requires:       libjpeg
Requires:       libksba-devel
Requires:       libksba
Requires:       libldb
Requires:       libmlx4
Requires:       libmng-devel
Requires:       libmng
Requires:       libmthca
Requires:       libnes
Requires:       libnl
Requires:       libnotify-devel
Requires:       libnotify
Requires:       libobjc
Requires:       libogg-devel
Requires:       libogg
Requires:       libpath_utils
Requires:       libpcap
Requires:       libpciaccess-devel
Requires:       libpciaccess
Requires:       libpng-devel
Requires:       libpng
Requires:       libraw1394
Requires:       librdmacm-devel
Requires:       librdmacm-utils
Requires:       librdmacm
Requires:       libref_array
Requires:       librsvg2
Requires:       libsane-hpaio
Requires:       libsdp
Requires:       libselinux-devel
Requires:       libselinux
Requires:       libselinux-python
Requires:       libselinux-utils
Requires:       libsemanage
Requires:       libsepol-devel
Requires:       libsepol
Requires:       libsigc++20
Requires:       libsmbclient
Requires:       libSM-devel
Requires:       libSM
Requires:       libsmi
Requires:       libsoup
Requires:       libstdc++44-devel
Requires:       libstdc++-devel
Requires:       libstdc++
Requires:       libsysfs
Requires:       libtalloc
Requires:       libtdb
Requires:       libtermcap-devel
Requires:       libtermcap
Requires:       libtevent
Requires:       libtidy
Requires:       libtiff-devel
Requires:       libtiff
Requires:       libtool-ltdl
Requires:       libtool
Requires:       libusb-devel
Requires:       libusb
Requires:       libuser-devel
Requires:       libuser
Requires:       libutempter
Requires:       libvolume_id
Requires:       libvorbis-devel
Requires:       libvorbis
Requires:       libwmf
Requires:       libwnck
Requires:       libwvstreams
Requires:       libX11-devel
Requires:       libX11
Requires:       libXau-devel
Requires:       libXau
Requires:       libXaw-devel
Requires:       libXaw
Requires:       libXcomposite-devel
Requires:       libXcomposite
Requires:       libXcursor-devel
Requires:       libXcursor
Requires:       libXdamage-devel
Requires:       libXdamage
Requires:       libXdmcp-devel
Requires:       libXdmcp
Requires:       libXevie-devel
Requires:       libXevie
Requires:       libXext-devel
Requires:       libXext
Requires:       libXfixes-devel
Requires:       libXfixes
Requires:       libXfontcache-devel
Requires:       libXfontcache
Requires:       libXfont-devel
Requires:       libXfont
Requires:       libXft-devel
Requires:       libXft
Requires:       libXi-devel
Requires:       libXi
Requires:       libXinerama-devel
Requires:       libXinerama
Requires:       libxkbfile
Requires:       libxml2-devel
Requires:       libxml2
Requires:       libxml2-python
Requires:       libXmu-devel
Requires:       libXmu
Requires:       libXp-devel
Requires:       libXp
Requires:       libXpm-devel
Requires:       libXpm
Requires:       libXrandr-devel
Requires:       libXrandr
Requires:       libXrender-devel
Requires:       libXrender
Requires:       libXres-devel
Requires:       libXres
Requires:       libXScrnSaver-devel
Requires:       libXScrnSaver
Requires:       libxslt-devel
Requires:       libxslt
Requires:       libXt-devel
Requires:       libXt
Requires:       libXTrap-devel
Requires:       libXTrap
Requires:       libXtst-devel
Requires:       libXtst
Requires:       libXv-devel
Requires:       libXvMC-devel
Requires:       libXvMC
Requires:       libXv
Requires:       libXxf86dga-devel
Requires:       libXxf86dga
Requires:       libXxf86misc-devel
Requires:       libXxf86misc
Requires:       libXxf86vm-devel
Requires:       libXxf86vm
Requires:       linuxwacom
Requires:       lm_sensors
Requires:       lockdev-devel
Requires:       lockdev
Requires:       log4cpp-devel
Requires:       log4cpp
Requires:       log4j
Requires:       logrotate
Requires:       logwatch
Requires:       lrzsz
Requires:       lslk
Requires:       lsof
Requires:       lsscsi
Requires:       ltrace
Requires:       lua
Requires:       lvm2
Requires:       lynx
Requires:       m2crypto
Requires:       m4
Requires:       mailcap
Requires:       mailx
Requires:       MAKEDEV
Requires:       make
Requires:       man-pages
Requires:       man-pages-overrides
Requires:       man
Requires:       mcelog
Requires:       mcstrans
Requires:       mc
Requires:       mdadm
Requires:       memtest86+
Requires:       mesa-libGL-devel
Requires:       mesa-libGL
Requires:       mesa-libGLU-devel
Requires:       mesa-libGLU
Requires:       mesa-libGLw-devel
Requires:       mesa-libGLw
Requires:       metacity
Requires:       mgetty
Requires:       microcode_ctl
Requires:       mingetty
Requires:       minicom
Requires:       mkbootdisk
Requires:       mkinitrd
Requires:       mktemp
Requires:       mlocate
Requires:       mod_auth_mysql
Requires:       module-init-tools
Requires:       mozldap
Requires:       mpi-selector
Requires:       mpitests-mvapich2
Requires:       mpitests-mvapich
Requires:       mpitests-openmpi
Requires:       mrtg
Requires:       mstflint
Requires:       mtools
Requires:       mtr
Requires:       mt-st
Requires:       mtx
Requires:       munge-libs
Requires:       munge
Requires:       mutt
Requires:       mvapich2
Requires:       mvapich
Requires:       mysql-bench
Requires:       mysql-connector-odbc
Requires:       mysql-devel
Requires:       MySQL-python
Requires:       mysql
Requires:       nano
Requires:       nash
Requires:       nasm
Requires:       nautilus-extensions
Requires:       ncurses-devel
Requires:       ncurses
Requires:       nc
Requires:       nedit
Requires:       neon
Requires:       netpbm-devel
Requires:       netpbm-progs
Requires:       netpbm
Requires:       net-snmp-libs
Requires:       net-snmp-utils
Requires:       net-snmp
Requires:       net-tools
Requires:       NetworkManager-glib
Requires:       NetworkManager
Requires:       newt-devel
Requires:       newt-perl
Requires:       newt
Requires:       nfs4-acl-tools
Requires:       nfs-utils-lib
Requires:       nfs-utils
Requires:       nmap-frontend
Requires:       nmap
Requires:       notification-daemon
Requires:       notify-python
Requires:       nscd
Requires:       nspr-devel
Requires:       nspr
Requires:       nss_db
Requires:       nss-devel
Requires:       nss_ldap
Requires:       nss-tools
Requires:       nss
Requires:       ntp
Requires:       ntsysv
Requires:       numactl
Requires:       numpy
Requires:       oddjob-libs
Requires:       oddjob
Requires:       ofed-docs
Requires:       openafs-compat
Requires:       openafs-firstboot
Requires:       openafs-krb5
Requires:       openafs
Requires:       openCryptoki
Requires:       openib
Requires:       OpenIPMI-gui
Requires:       OpenIPMI-libs
Requires:       OpenIPMI-python
Requires:       OpenIPMI-tools
Requires:       OpenIPMI
Requires:       openjade
Requires:       openldap-clients
Requires:       openldap-devel
Requires:       openldap
Requires:       openldap-servers-overlays
Requires:       openldap-servers
Requires:       openmotif22
Requires:       openmotif-devel
Requires:       openmotif
Requires:       openmpi-devel
Requires:       openmpi-libs
Requires:       openmpi
Requires:       openscap
Requires:       opensm-libs
Requires:       opensm
Requires:       opensp
Requires:       openssh-askpass
Requires:       openssh-clients
Requires:       openssh
Requires:       openssl097a
Requires:       openssl-devel
Requires:       openssl
Requires:       openswan
Requires:       oprofile
Requires:       ORBit2-devel
Requires:       ORBit2
Requires:       pam_ccreds
Requires:       pam-devel
Requires:       pam
Requires:       pam_krb5
Requires:       pam_passwdqc
Requires:       pam_pkcs11
Requires:       pam_smb
Requires:       pango-devel
Requires:       pango
Requires:       paps
Requires:       parted
Requires:       passwd
Requires:       patchutils
Requires:       patch
Requires:       pax
Requires:       pciutils-devel
Requires:       pciutils
Requires:       pcmciautils
Requires:       pcre
Requires:       pcsc-lite-devel
Requires:       pcsc-lite-libs
Requires:       pcsc-lite
Requires:       perftest
Requires:       perl-Archive-Zip
Requires:       perl-Authen-SASL
Requires:       perl-Class-Inspector
Requires:       perl-common-sense
Requires:       perl-Compress-Zlib
Requires:       perl-Convert-ASN1
Requires:       perl-Convert-BinHex
Requires:       perl-Crypt-DES
Requires:       perl-Crypt-SSLeay
Requires:       perl-DBD-MySQL
Requires:       perl-DBI
Requires:       perl-Digest-HMAC
Requires:       perl-Digest-SHA1
Requires:       perl-GSSAPI
Requires:       perl-HTML-Parser
Requires:       perl-HTML-Tagset
Requires:       perl-IO-Socket-INET6
Requires:       perl-IO-Socket-SSL
Requires:       perl-IO-String
Requires:       perl-IO-stringy
Requires:       perl-JSON-XS
Requires:       perl-LDAP
Requires:       perl-libwww-perl
Requires:       perl-libxml-perl
Requires:       perl-MailTools
Requires:       perl-MIME-Lite
Requires:       perl-MIME-tools
Requires:       perl-Mozilla-LDAP
Requires:       perl-Net-Jabber
Requires:       perl-Net-SNMP
Requires:       perl-Net-SSLeay
Requires:       perl-Net-XMPP
Requires:       perl-parent
Requires:       perl-Pod-POM
Requires:       perl-Proc-ProcessTable
Requires:       perl-SOAP-Lite
Requires:       perl-Socket6
Requires:       perl-String-CRC32
Requires:       perl-TeX-Hyphen
Requires:       perl-Text-Autoformat
Requires:       perl-Text-Reform
Requires:       perl-TimeDate
Requires:       perl-Time-modules
Requires:       perl-URI
Requires:       perl
Requires:       perl-XML-Dumper
Requires:       perl-XML-Grove
Requires:       perl-XML-NamespaceSupport
Requires:       perl-XML-Parser
Requires:       perl-XML-SAX
Requires:       perl-XML-Simple
Requires:       perl-XML-Stream
Requires:       perl-XML-Twig
Requires:       pexpect
Requires:       php
Requires:       php-common
Requires:       php-mysql
Requires:       php-pdo
Requires:       pinentry
Requires:       pinfo
Requires:       pirut
Requires:       pkgconfig
Requires:       pkinit-nss
Requires:       pm-utils
Requires:       policycoreutils-gui
Requires:       policycoreutils
Requires:       poppler-utils
Requires:       poppler
Requires:       popt
Requires:       portmap
Requires:       postgresql-libs
Requires:       ppp
Requires:       prelink
Requires:       privoxy
Requires:       procmail
Requires:       procps
Requires:       psacct
Requires:       psgml
Requires:       psmisc
Requires:       pstack
Requires:       psutils
Requires:       pth-devel
Requires:       pth
Requires:       pvm
Requires:       pycairo
Requires:       pygobject2
Requires:       pygtk2-libglade
Requires:       pygtk2
Requires:       pyOpenSSL
Requires:       pyorbit
Requires:       pyparted
Requires:       PyQt
Requires:       pyspi
Requires:       python26-libs
Requires:       python26
Requires:       python-devel
Requires:       python-dmidecode
Requires:       python-docs
Requires:       python-elementtree
Requires:       python-imaging
Requires:       python-iniparse
Requires:       python-ldap
Requires:       python-libs
Requires:       python-nose
Requires:       python-numeric
Requires:       python-setuptools
Requires:       python-sqlite
Requires:       python-suds
Requires:       python-urlgrabber
Requires:       python
Requires:       pyxf86config
Requires:       PyXML
Requires:       qlvnictools
Requires:       qperf
Requires:       qt-MySQL
Requires:       qt
Requires:       quagga
Requires:       quota
Requires:       radvd
Requires:       rcs
Requires:       rdate
Requires:       rdist
Requires:       rds-tools
Requires:       readahead
Requires:       readline-devel
Requires:       readline
Requires:       redhat-artwork
Requires:       redhat-logos
Requires:       redhat-lsb
Requires:       redhat-menus
Requires:       redhat-rpm-config
Requires:       rhgb
Requires:       rhpl
Requires:       rhpxl
Requires:       rmt
Requires:       rng-utils
Requires:       rootfiles
Requires:       rpm-build
Requires:       rpm-devel
Requires:       rpm-libs
Requires:       rpm-python
Requires:       rpm
Requires:       rp-pppoe
Requires:       rsh
Requires:       rsync
Requires:       rsyslog
Requires:       rt61pci-firmware
Requires:       rt73usb-firmware
Requires:       SAGA.lsu-cpp.engine
Requires:       samba3x-common
Requires:       samba3x-winbind
Requires:       sane-backends-libs
Requires:       sane-backends
Requires:       sane-frontends
Requires:       sblim-cmpi-dhcp-devel
Requires:       sblim-cmpi-dhcp
Requires:       sblim-gather
Requires:       sblim-tools-libra
Requires:       sblim-wbemcli
Requires:       scipy
Requires:       screen
Requires:       scrollkeeper
Requires:       SDL-devel
Requires:       SDL
Requires:       sed
Requires:       selinux-policy-devel
Requires:       selinux-policy
Requires:       selinux-policy-targeted
Requires:       sendmail-cf
Requires:       sendmail
Requires:       setarch
Requires:       setools
Requires:       setserial
Requires:       setup
Requires:       setuptool
Requires:       sgml-common
Requires:       sgpio
Requires:       shadow-utils
Requires:       shared-mime-info
Requires:       sharutils
Requires:       sip
Requires:       SL_afs_no_dynroot
Requires:       slang-devel
Requires:       slang
Requires:       SL_password_for_singleuser
Requires:       sl-release
Requires:       sl-release-notes
Requires:       slrn
Requires:       SL_rpm_show_arch
Requires:       SL_sendmail_accept
Requires:       smartmontools
Requires:       sos
Requires:       sox
Requires:       specspo
Requires:       splint
Requires:       sqlite-devel
Requires:       sqlite
Requires:       squashfs-tools
Requires:       srm-ifce
Requires:       srptools
Requires:       sssd-client
Requires:       sssd
Requires:       startup-notification-devel
Requires:       startup-notification
Requires:       star
Requires:       statserial
Requires:       strace
Requires:       stunnel
Requires:       subversion
Requires:       sudo
Requires:       suitesparse
Requires:       svrcore
Requires:       swig
Requires:       switchdesk
Requires:       symlinks
Requires:       synaptics
Requires:       sysfsutils
Requires:       sysklogd
Requires:       syslinux
Requires:       sysstat
Requires:       system-config-date
Requires:       system-config-display
Requires:       system-config-keyboard
Requires:       system-config-language
Requires:       system-config-network
Requires:       system-config-network-tui
Requires:       system-config-printer-libs
Requires:       system-config-printer
Requires:       system-config-securitylevel-tui
Requires:       system-config-securitylevel
Requires:       system-config-services
Requires:       system-config-soundcard
Requires:       system-config-users
Requires:       systemtap-runtime
Requires:       systemtap
Requires:       SysVinit
Requires:       talk
Requires:       tar
Requires:       tcl
Requires:       tclx
Requires:       tcpdump
Requires:       tcp_wrappers
Requires:       tcsh
Requires:       telnet
Requires:       termcap
Requires:       texinfo
Requires:       tftp
Requires:       tidy
Requires:       time
Requires:       tix
Requires:       tk
Requires:       tkinter
Requires:       tmpwatch
Requires:       tn5250
Requires:       tog-pegasus-devel
Requires:       tog-pegasus-libs
Requires:       tog-pegasus
Requires:       tpm-tools
Requires:       traceroute
Requires:       transfig
Requires:       tree
Requires:       trousers
Requires:       ttmkfdir
Requires:       tvflash
Requires:       tzdata-java
Requires:       tzdata
Requires:       uberftp
Requires:       udev
Requires:       udftools
Requires:       unifdef
Requires:       units
Requires:       unix2dos
Requires:       unixODBC-libs
Requires:       unixODBC
Requires:       unzip
Requires:       urw-fonts
Requires:       usbutils
Requires:       usermode-gtk
Requires:       usermode
Requires:       util-linux
Requires:       uucp
Requires:       uuidd
Requires:       valgrind
Requires:       vconfig
Requires:       vim-common
Requires:       vim-enhanced
Requires:       vim-minimal
Requires:       vim-X11
Requires:       virt-what
Requires:       vixie-cron
Requires:       vlock
Requires:       vnc-server
Requires:       vnc
Requires:       vte
Requires:       wacomexpresskeys
Requires:       watchdog
Requires:       wdaemon
Requires:       wget
Requires:       which
Requires:       wireless-tools
Requires:       wireshark-gnome
Requires:       wireshark
Requires:       words
Requires:       wpa_supplicant
Requires:       wvdial
Requires:       x3270
Requires:       x86info
Requires:       Xaw3d-devel
Requires:       Xaw3d
Requires:       xbae
Requires:       xdelta
Requires:       xerces-c
Requires:       xfig
Requires:       xinetd
Requires:       xkeyboard-config
Requires:       xml-common
Requires:       xmlrpc-c-client
Requires:       xmlrpc-c
Requires:       xmlsec1-devel
Requires:       xmlsec1
Requires:       xorg-x11-apps
Requires:       xorg-x11-drivers
Requires:       xorg-x11-drv-acecad
Requires:       xorg-x11-drv-aiptek
Requires:       xorg-x11-drv-ast
Requires:       xorg-x11-drv-ati
Requires:       xorg-x11-drv-calcomp
Requires:       xorg-x11-drv-cirrus
Requires:       xorg-x11-drv-citron
Requires:       xorg-x11-drv-digitaledge
Requires:       xorg-x11-drv-dmc
Requires:       xorg-x11-drv-dummy
Requires:       xorg-x11-drv-dynapro
Requires:       xorg-x11-drv-elo2300
Requires:       xorg-x11-drv-elographics
Requires:       xorg-x11-drv-evdev
Requires:       xorg-x11-drv-fbdev
Requires:       xorg-x11-drv-fpit
Requires:       xorg-x11-drv-hyperpen
Requires:       xorg-x11-drv-i810
Requires:       xorg-x11-drv-jamstudio
Requires:       xorg-x11-drv-joystick
Requires:       xorg-x11-drv-keyboard
Requires:       xorg-x11-drv-magellan
Requires:       xorg-x11-drv-magictouch
Requires:       xorg-x11-drv-mga
Requires:       xorg-x11-drv-microtouch
Requires:       xorg-x11-drv-mouse
Requires:       xorg-x11-drv-mutouch
Requires:       xorg-x11-drv-nv
Requires:       xorg-x11-drv-palmax
Requires:       xorg-x11-drv-penmount
Requires:       xorg-x11-drv-qxl
Requires:       xorg-x11-drv-s3virge
Requires:       xorg-x11-drv-s3
Requires:       xorg-x11-drv-savage
Requires:       xorg-x11-drv-siliconmotion
Requires:       xorg-x11-drv-sisusb
Requires:       xorg-x11-drv-sis
Requires:       xorg-x11-drv-spaceorb
Requires:       xorg-x11-drv-summa
Requires:       xorg-x11-drv-tdfx
Requires:       xorg-x11-drv-tek4957
Requires:       xorg-x11-drv-trident
Requires:       xorg-x11-drv-ur98
Requires:       xorg-x11-drv-vesa
Requires:       xorg-x11-drv-vga
Requires:       xorg-x11-drv-via
Requires:       xorg-x11-drv-vmmouse
Requires:       xorg-x11-drv-vmware
Requires:       xorg-x11-drv-void
Requires:       xorg-x11-drv-voodoo
Requires:       xorg-x11-filesystem
Requires:       xorg-x11-fonts-100dpi
Requires:       xorg-x11-fonts-75dpi
Requires:       xorg-x11-fonts-base
Requires:       xorg-x11-fonts-ISO8859-1-100dpi
Requires:       xorg-x11-fonts-ISO8859-1-75dpi
Requires:       xorg-x11-fonts-misc
Requires:       xorg-x11-fonts-truetype
Requires:       xorg-x11-fonts-Type1
Requires:       xorg-x11-font-utils
Requires:       xorg-x11-proto-devel
Requires:       xorg-x11-resutils
Requires:       xorg-x11-server-sdk
Requires:       xorg-x11-server-utils
Requires:       xorg-x11-server-Xnest
Requires:       xorg-x11-server-Xorg
Requires:       xorg-x11-server-Xvfb
Requires:       xorg-x11-twm
Requires:       xorg-x11-util-macros
Requires:       xorg-x11-utils
Requires:       xorg-x11-xauth
Requires:       xorg-x11-xbitmaps
Requires:       xorg-x11-xdm
Requires:       xorg-x11-xfs-utils
Requires:       xorg-x11-xfs
Requires:       xorg-x11-xfwp
Requires:       xorg-x11-xinit
Requires:       xorg-x11-xkb-utils
Requires:       xorg-x11-xsm
Requires:       xorg-x11-xtrans-devel
Requires:       xrestop
Requires:       xsane-gimp
Requires:       xsane
Requires:       xsri
Requires:       xterm
Requires:       xulrunner-devel
Requires:       xulrunner
Requires:       xz-libs
Requires:       xz
Requires:       yelp
Requires:       ypbind
Requires:       ypserv
Requires:       yp-tools
Requires:       yum-autoupdate
Requires:       yum-conf
Requires:       yum-downloadonly
Requires:       yum-metadata-parser
Requires:       yum
Requires:       yum-utils
Requires:       zip
Requires:       zisofs-tools
Requires:       zlib-devel
Requires:       zlib
Requires:       zsh
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
* Thu May 13 2014 Yan Xiaofei <yanxf@ihep.ac.cn> - 1.0.0-2
- delete zefs
* Thu Apr 10 2014 Yan Xiaofei <yanxf@ihep.ac.cn> - 1.0.0-1
- First version for wn58pkg
