#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : overtest
Version  : 0.14.0
Release  : 6
URL      : https://pypi.python.org/packages/source/o/overtest/overtest-0.14.0.tar.gz
Source0  : https://pypi.python.org/packages/source/o/overtest/overtest-0.14.0.tar.gz
Summary  : Suite of tools to manage daemons for testing
Group    : Development/Tools
License  : Apache-2.0
Requires: overtest-bin
Requires: overtest-python
Requires: overtest-data
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
==========
Overtest
==========
Overtest is a suite of tools that allows to start and stop daemons for a quick
throw-away usage. This is typically useful when needing these daemons to run
`integration testing`_.

%package bin
Summary: bin components for the overtest package.
Group: Binaries
Requires: overtest-data

%description bin
bin components for the overtest package.


%package data
Summary: data components for the overtest package.
Group: Data

%description data
data components for the overtest package.


%package python
Summary: python components for the overtest package.
Group: Default

%description python
python components for the overtest package.


%prep
%setup -q -n overtest-0.14.0

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/overtest

%files data
%defattr(-,root,root,-)
/usr/share/overtest/lib/_utils
/usr/share/overtest/lib/elasticsearch
/usr/share/overtest/lib/etcd
/usr/share/overtest/lib/gnocchi
/usr/share/overtest/lib/influxdb
/usr/share/overtest/lib/memcached
/usr/share/overtest/lib/mongodb
/usr/share/overtest/lib/mysql
/usr/share/overtest/lib/postgresql
/usr/share/overtest/lib/redis
/usr/share/overtest/lib/zookeeper

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
