# Copyright © 2021 rdbende <rdbende@gmail.com>

# A stunning dark theme for ttk based on Microsoft's Sun Valley visual style 

package require Tk 8.6

namespace eval ttk::theme::sun-valley-dark {
    variable version 1.0
    package provide ttk::theme::sun-valley-dark $version

    ttk::style theme create sun-valley-dark -parent clam -settings {
        proc load_images {imgdir} {
            variable images
            foreach file [glob -directory $imgdir *.png] {
                set images([file tail [file rootname $file]]) \
                [image create photo -file $file -format png]
            }
        }

        load_images [file join [file dirname [info script]] dark]

        array set colors {
            -fg             "#ffffff"
            -bg             "#1c1c1c"
            -disabledfg     "#595959"
            -selectfg       "#ffffff"
            -selectbg       "#2f60d8"
        }

        ttk::style layout Accent.TButton {
            AccentButton.button -children {
                AccentButton.padding -children {
                    AccentButton.label -side left -expand 1
                } 
            }
        }
     
        # Button
        ttk::style configure TButton -padding {8 4} -anchor center -foreground $colors(-fg)

        ttk::style map TButton -foreground \
            [list disabled #7a7a7a \
                pressed #d0d0d0]

        ttk::style element create Button.button image \
            [list $images(button-rest) \
                {selected disabled} $images(button-disabled) \
                disabled $images(button-disabled) \
                selected $images(button-rest) \
                pressed $images(button-pressed) \
                active $images(button-hover) \
            ] -border 4 -sticky nsew


        # Accent.TButton
        ttk::style configure Accent.TButton -padding {8 4} -anchor center -foreground #000000

        ttk::style map Accent.TButton -foreground \
            [list pressed #25536a \
                disabled #a5a5a5]

        ttk::style element create AccentButton.button image \
            [list $images(button-accent-rest) \
                {selected disabled} $images(button-accent-disabled) \
                disabled $images(button-accent-disabled) \
                selected $images(button-accent-rest) \
                pressed $images(button-accent-pressed) \
                active $images(button-accent-hover) \
            ] -border 4 -sticky nsew

        # Entry
        ttk::style configure TEntry -foreground $colors(-fg)

        ttk::style map TEntry -foreground \
            [list disabled #757575 \
                pressed #cfcfcf
            ]

        ttk::style element create Entry.field \
            image [list $images(entry-rest) \
                {focus hover !invalid} $images(entry-focus) \
                invalid $images(entry-invalid) \
                disabled $images(entry-disabled) \
                {focus !invalid} $images(entry-focus) \
                hover $images(entry-hover) \
            ] -border 5 -padding 8 -sticky nsew

    }
}