 Changelog
 =========

All noteable changes to this project, *colab-repoclone*, will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Added
 - N/A

### Changed
 - N/A

### Removed
 - N/A


## [0.2.3] - 2019-07-11

Renamed branch method due to conflict with branch attribute


## [0.2.2] - 2019-07-11

Fixed logic bug with error checking


## [0.2.1] - 2019-07-11

Fixed a really stupid bug


## [0.2.0] - 2019-07-11

Added significant functionality, including methods for creating and checking-out new
branches and for resetting to a prior commit. Also made minor changes to formatting,
code flow and user input fields.

### Added
 - branch() method
 - checkout() method
 - reset() method
 - Warnings before pushing and resetting

### Changed
 - Failure checks now occur after each shell call to stop errors from carrying over
 - Expanded upon some error messages to make more informative
 - Edited wording of user input fields
 - Pushing now requires you enter a commit message (there is no default)
 - Updated README with new functionalities


## [0.1.5] - 2019-07-10

Fixed bug with initializing new repository functionality


## [0.1.4] - 2019-07-10

Very minor formatting changes


## [0.1.3] - 2019-07-10

Minor formatting changes

### Changes
 - "method" keyword to "auth_method" for clarity


## [0.1.2] - 2019-07-10

Added capability to initialize new repositories directly from Colab. A few other minor
changes and reformatting

### Added
 - Initialize repo with existing folder capability


## [0.1.1] - 2019-07-10

Added additional "change directory" commands to ensure files end up in the right place.
A few other minor changes

### Added
 - Multiple os.chdir commands


## [0.1.0] - 2019-07-10

Fixed commit issue, added more descriptive error messages and removed masking when user 
inputs GitHub username and email

### Added
 - Descriptive error messages

### Changed
 - 'git commit' command
 - Masking when entering username and email


## [0.0.2] - 2019-07-10

Minor changes and added MANIFEST to fix build issues

### Added
 - MANIFEST.in


## [0.0.1] - 2019-07-09

Initial version. Handles github integration for pushing and pulling to/from repositories
directly from Google Colab.
