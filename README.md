# Narcotic sounds generator
Assignment for python course

## How to use

```shell
> python NarcoticGenerator.py results/out.mid --bmp 180 --inst piano
```

```
usage: NarcoticGenerator.py [-h] [--type TYPE] [--inst INST] [--bpm BPM]
                            [--length LENGTH] [--rand RAND]

Generate track

positional arguments:
  OUTPUT_FILE      Set output file path

optional arguments:
  -h, --help       show this help message and exit
  --type TYPE      Set genre: jazz, movie, hiphop, rock
  --inst INST      Set instrument: guitar,piano,bird,violin,trumpet
  --bpm BPM        Set beats per minute
  --length LENGTH  Set track length (min)
  --rand RAND      Add random notes to track: True, False

```

## Required Libraries

 - midiutil
 - mido
