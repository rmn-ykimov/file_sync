# **THIS REPO IS ARCHIVED**

---

# Project Objective

The goal of this project is to develop a program that will ensure that the
content of two folders, "source" and "replica", remains identical. The program
will periodically perform a one-way synchronization of the source folder to the
replica folder, ensuring that any changes made to the source folder are
reflected in the replica folder.

---

# Key Requirements

## One-way Synchronization

The content of the replica folder should match the source folder after each
synchronization.

## Periodic Synchronization

The program should perform the synchronization at a specified time interval.

## Logging

The program should log all file creation, copying, and removal operations to
both a log file and the console output.

---

# Inputs

## Folder Paths

The paths to the source and replica folders must be specified.

## Synchronization Interval

The interval at which the synchronization should occur must be specified.

## Log File Path

The path to the log file must be specified.

---

# Libraries

## Third-Party Library Restrictions

The use of third-party libraries for folder synchronization is discouraged.

## Recommended Libraries

The use of third-party or built-in libraries for other algorithms, such as MD5
calculation, is allowed and recommended.
