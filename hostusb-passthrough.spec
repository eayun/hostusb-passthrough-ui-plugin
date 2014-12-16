%define _version 1.0
%define _release 1

Name:		hostusb-passthrough
Version:	%{_version}
Release:	%{_release}%{?dist}
Summary:	UI Plugin for hostusb passthrough function

Group:		ovirt-engine-third-party
License:	GPL
URL:		http://www.eayun.com
Source0:	hostusb-passthrough-%{_version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch

BuildRequires:	/bin/bash
Requires:	ovirt-engine >= 3.5.0
Requires:	patternfly1

%description

%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/
cp hostusb-passthrough.json %{buildroot}/usr/share/ovirt-engine/ui-plugins/
cp hostusb-passthrough-resources/plugin.html %{buildroot}/usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/
cp hostusb-passthrough-resources/hostusb-passthrough.html %{buildroot}/usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/

%clean
rm -rf %{buildroot}

%post
ln -s /usr/share/patternfly1/resources/css /usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/css
ln -s /usr/share/patternfly1/resources/js /usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/js


%files
%defattr(-,root,root,-)
/usr/share/ovirt-engine/ui-plugins/hostusb-passthrough.json
/usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/

%postun
unlink /usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/css
unlink /usr/share/ovirt-engine/ui-plugins/hostusb-passthrough-resources/js


%changelog

* Fri Nov 21 2014 MaZhe <liyang.pan@eayun.com> 1.0-1
- First build

