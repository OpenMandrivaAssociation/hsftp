%define name    hsftp 
%define version 1.15
%define release  %mkrel 1

Summary: FTP-type client using SSH to transfer files 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL 
URL: http://la-samhna.de/hsftp/
Group: Networking/File transfer
Prefix: %{_prefix}
Requires: openssh-clients

%description
hsftp is an FTP emulator that provides the look and feel of an FTP session,
but uses ssh to transport commands and data. It is written in C, and requires
no additional libraries.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{name}-%{version}

%build

%configure

%make

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc readme license hsftp.lsm
%{_bindir}/*
%{_mandir}/man1/*.1*

