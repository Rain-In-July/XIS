from cargo import Cargo

cargo = Cargo(id='oil_sands',
              unit_name='string(STR_CARGO_NAME_OIL_SANDS)',
              type_name='string(STR_CARGO_NAME_OIL_SANDS)',
              type_abbreviation='string(STR_CID_OIL_SANDS)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='53',
              is_freight='1',
              cargo_classes='bitmask(CC_BULK)',
              cargo_label='OSND',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_OIL_SANDS)',
              penalty_lowerbound='30',
              single_penalty_length='255',
              price_factor='95',
              capacity_multiplier='1',
              icon_indices=(6, 4))
