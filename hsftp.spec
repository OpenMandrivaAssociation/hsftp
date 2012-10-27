Summary:	FTP-type client using SSH to transfer files 
Name:		hsftp
Version:	1.15
Release:	5
Source0:	%{name}-%{version}.tar.bz2
Patch0:		hsftp-1.15-fix-string-format.patch
License:	GPL 
URL:		http://la-samhna.de/hsftp/
Group:		Networking/File transfer
Requires:	openssh-clients

%description
hsftp is an FTP emulator that provides the look and feel of an FTP session,
but uses ssh to transport commands and data. It is written in C, and requires
no additional libraries.

%prep
%setup -q
%patch0 -p1 -b .str_fmt~

%build
%configure
%make

%install
%makeinstall

%files
%doc readme license hsftp.lsm
%{_bindir}/*
%{_mandir}/man1/*.1*
