
class MissingCSVFileError(Exception):
    """
    Exception when a *.csv file is
    missing in the request.
    """

    msg = "CSV file is not send via request."

    def __str__(self):
        return self.msg


class CSVMergeError(Exception):
    """
    Exception when merge/enrich *.csv file already
    uploaded in the application.
    """

    msg = "Exception while merging stored *.csv file with external fetched via API."

    def __str__(self):
        return self.msg


class CSVNotSavedError(Exception):
    """
    Exception when csv file can not be saved in the mounted location.
    """

    msg = "File *.csv was not saved."

    def __str__(self):
        return self.msg
