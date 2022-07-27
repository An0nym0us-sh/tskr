# tskr

Use the command line to create and edit tasks

## setup
Run the setup.sh to set up tskr. tskr only
needs 2 files. The binary and the task list. By 
default these are stored at:

- ~/.local/bin/tskr (binary)
- ~/.local/share/tskr/tskr\_tasks (task list)

## help
Commands are passed in as just words

(All dates should be passed in the YYYY-MM-DD format)

Available Commands:

```
    new : 
        create a new task. Look at the example below.
        tskr new 2022-02-10 Observe Umbrella Day
    remove:
        remove a task from the task list 
        tskr remove 1 (This removes the first task)
    clear:
        clear al tasks from the list.
        tskr clear 
    set:
        use this to set the status and time of tasks (You can set statuses to any one word)
        tskr set status skippable n (sets the status of the nth task in the task list)
        tskr set time 2022-09-3 n (set the time of the nth task in the task list)
```

`Warning`: tskr doesn't validate input so invalid inputs should result in (most probably) harmless errors from python
