%global packname  mix
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.8
Release:          1
Summary:          Estimation/multiple Imputation for Mixed Categorical and Continuous Data
Group:            Sciences/Mathematics
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/mix_1.0-8.tar.gz
Requires:         R-stats 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats

%description
Estimation/multiple imputation programs for mixed categorical and
continuous data

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_8-1
+ Revision: 775856
- Import R-mix
- Import R-mix


