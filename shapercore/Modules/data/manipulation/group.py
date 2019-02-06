from shapercore.Modules.metaclass.Module_Data import Data


class Group(Data):
    def __init__(self, name, columns):
        self._name = name
        self._columns = columns

    def visit(self, featureset):
        try:
            target = str(self._name)
            frame = featureset.get_dataframe()

            # create new column (containing matrix)
            frame[target] = list(frame[self._columns].values)

            # get correct index for new column
            columns = list(frame)
            lowest_index = len(columns) - 1
            for column in columns:
                if column in self._columns:
                    lowest_index = columns.index(column)

            # insert column name into columns-list and drop last entry
            columns.insert(lowest_index, target)
            columns.pop()

            # reindex list, drop not-grouped columns
            frame = frame.reindex(columns, axis=1)
            frame = frame.drop(columns=self._columns, axis=1)

            featureset.set_dataframe(frame)

        except Exception as error:
            Util.print_error("Unable to Group Features: " + str(error))
            Util.print_detailed_error()
